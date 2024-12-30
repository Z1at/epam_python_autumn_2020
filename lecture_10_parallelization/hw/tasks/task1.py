"""
Homework

Ваша задача спарсить информацию о компаниях,
находящихся в индексе S&P 500 с данного сайта:
https://markets.businessinsider.com/index/components/s&p_500

Для каждой компании собрать следующую информацию:

    Текущая стоимость в рублях (конвертацию производить по текущему курсу,
взятому с сайта центробанка РФ)
    Код компании (справа от названия компании на странице компании)
    P/E компании (информация находится справа от графика на странице компании)
    Годовой рост/падение компании в процентах (основная таблица)
    Высчитать какую прибыль принесли бы акции компании (в процентах),
если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High
(справа от графика на странице компании)

Сохранить итоговую информацию в 4 JSON файла:

    Топ 10 компаний с самими дорогими акциями в рублях.
    Топ 10 компаний с самым низким показателем P/E.
    Топ 10 компаний, которые показали самый высокий рост за последний год
    Топ 10 комппаний, которые принесли бы наибольшую прибыль,
если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.

Пример формата:

[
{
    "code": "MMM",
    "name": "3M CO.",
    "price" | "P/E" | "growth" | "potential profit" : value,
},
...
]

For scrapping you cans use beautifulsoup4
For requesting aiohttp

"""
import asyncio
import datetime
import json
import re

import aiohttp
import requests
from bs4 import BeautifulSoup, SoupStrainer


def create_files(companies, metrics):
    """Creates a json file. Each file is named by its own metric.

    Args:
        companies: A generator that yields the company and its values.
        metrics: Dictionary with metrics.

    """
    for metric_num in metrics:
        with open(f"{metrics[metric_num]}.json", "w") as f:
            json.dump(next(companies), f, indent=4)


def sort_companies(companies, metrics):
    """A generator that sorts companies by metrics.
    And then yields only a list of top companies.

    Args:
        companies: A dictionary with a key as the company code and
        value as company metrics.

        metrics: Dictionary with metrics.

    Returns:
        A generator that yields only a list of top companies for a specific metric.

    """
    for metric_num in metrics:
        companies = {
            company_code: companies[company_code]
            for company_code in sorted(
                companies,
                key=lambda key: companies[key][metric_num],
                reverse=True if metric_num != 2 else False,
            )
        }

        top_companies = []
        for num, company_code in enumerate(companies):
            data_the_about_top_company = {
                "code": company_code,
                "name": companies[company_code][0],
                f"{metrics[metric_num]}": companies[company_code][metric_num],
            }

            top_companies.append(data_the_about_top_company)

            if num == 9:
                break

        yield top_companies


def ratio_of_ruble_to_dollar():
    """Knows the ratio of the ruble to the dollar.

    Returns:
        Price of one dollar in rubles.

    """
    today = datetime.date.today()
    today_in_russian = today.strftime("%d/%m/%Y")

    response = requests.get(
        f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1="
        f"{today_in_russian}"
        f"&date_req2=01/01/2049&VAL_NM_RQ=R01235"
    )

    soup = BeautifulSoup(response.text, "lxml")

    return float(soup.find("value").text.replace(",", "."))


async def getting_text_from_urls(url, company_code=None):
    """Returns the html text of the url.

    Args:
        url: URL.
        company_code: Company code if necessary.

    Returns:
        The html text

    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            if company_code:
                return await response.text(), company_code
            return await response.text()


async def processing_data_on_companies(the_raw_data_of_the_companies):
    """Takes the raw data of the companies with the extra tags.
    And then only the necessary remains, i.e.
    company code, company name, price, P/E, growth, potential profit.

    Args:
        the_raw_data_of_the_companies: A list of raw data for each company.

    Returns:
        A dictionary where the key is the company code and
        the values are the company metrics.

    """
    information_about_companies = {}

    urls_and_codes_of_all_companies = []
    for company in the_raw_data_of_the_companies:
        raw_company_page = company.find("a")
        pattern = r".*\/([\w]*)-.*"
        the_url_of_the_company = (
            "https://markets.businessinsider.com/" + raw_company_page["href"]
        )
        company_code = str.upper(re.sub(pattern, r"\1", raw_company_page["href"]))
        company_name = raw_company_page["title"]
        urls_and_codes_of_all_companies.append([the_url_of_the_company, company_code])

        the_raw_price_of_the_shares = company.find("td", class_="text-right")
        the_price_of_the_shares = float(
            the_raw_price_of_the_shares.contents[0].replace(",", "")
        )

        the_raw_company_growth_in_one_year = company.find_all("span", class_=True)
        the_company_growth_in_one_year = float(
            the_raw_company_growth_in_one_year[-1].contents[0][:-1].replace(",", "")
        )

        # company code: [company name, price, P/E, growth, potential profit]
        information_about_companies[company_code] = [
            company_name,
            the_price_of_the_shares,
            float("inf"),
            the_company_growth_in_one_year,
            0,
        ]

    tasks = [
        asyncio.create_task(getting_text_from_urls(*company_url_and_code))
        for company_url_and_code in urls_and_codes_of_all_companies
    ]

    await asyncio.gather(*tasks)

    only_price_to_earnings_ratio = SoupStrainer("div", class_="snapshot__data-item")
    pattern_price_to_earnings_ratio = re.compile(r"([0-9]*\.[0-9]*)\r\n.*P/E Ratio")

    only_high_and_low_for_52_weeks = SoupStrainer("script")
    pattern_high = re.compile(r"high52weeks: ([0-9]*\.[0-9]*)")
    pattern_low = re.compile(r"low52weeks: ([0-9]*\.[0-9]*)")

    for company_url_and_code in tasks:
        html, company_code = company_url_and_code.result()

        soup = BeautifulSoup(html, "lxml", parse_only=only_price_to_earnings_ratio)

        price_to_earnings_ratio = float("inf")
        soup_text = soup.text
        if soup_text:
            match = pattern_price_to_earnings_ratio.search(soup_text)
            if match:
                price_to_earnings_ratio = float(match.group(1))
                price_to_earnings_ratio = (
                    float("inf")
                    if price_to_earnings_ratio < 0
                    else price_to_earnings_ratio
                )

        soup = BeautifulSoup(html, "lxml", parse_only=only_high_and_low_for_52_weeks)

        high52weeks = 0
        script = str(soup.find("script", text=pattern_high))
        if script:
            match = pattern_high.search(script)
            if match:
                high52weeks = float(match.group(1))

        low52weeks = 0
        script = str(soup.find("script", text=pattern_low))
        if script:
            match = pattern_low.search(script)
            if match:
                low52weeks = float(match.group(1))

        information_about_companies[company_code][2] = price_to_earnings_ratio
        if low52weeks:
            information_about_companies[company_code][4] = round(
                high52weeks * 100 / low52weeks - 100, 2
            )

    return information_about_companies


async def collecting_data_about_companies(num_of_pages=10):
    """Collects pages that store data about all companies.
    And after processing the data, we get raw data for each company.

    Args:
        num_of_pages: The number of pages required.

    Returns:
        A list of raw data for each company

    """
    initial_url = "https://markets.businessinsider.com/index/components/s&p_500"
    tasks = [
        asyncio.create_task(getting_text_from_urls(initial_url + f"?p={i}"))
        for i in range(1, num_of_pages + 1)
    ]

    await asyncio.gather(*tasks)

    only_the_lines_about_the_companies = SoupStrainer("tr")
    the_data_about_the_companies = []
    for html in tasks:
        soup = BeautifulSoup(
            html.result(), "lxml", parse_only=only_the_lines_about_the_companies
        )
        the_data_about_the_companies.extend(soup.find_all("tr")[2:])

    return the_data_about_the_companies


if __name__ == "__main__":
    raw_data_about_companies = asyncio.get_event_loop().run_until_complete(
        collecting_data_about_companies()
    )

    data_about_companies = asyncio.get_event_loop().run_until_complete(
        processing_data_on_companies(raw_data_about_companies)
    )

    num_of_rubles_to_dollar = ratio_of_ruble_to_dollar()
    for company_data in data_about_companies:
        data_about_companies[company_data][1] = round(
            data_about_companies[company_data][1] * num_of_rubles_to_dollar, 2
        )

    list_of_metrics = {1: "price", 2: "P_E", 3: "growth", 4: "potential_profit"}
    gen = sort_companies(data_about_companies, list_of_metrics)
    create_files(gen, list_of_metrics)
