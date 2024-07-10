from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json
import csv
import time

def setup_driver():
    options = Options()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    return driver

def wait_for_page_to_load(driver, by, value, timeout=10):
    wait = WebDriverWait(driver, timeout)
    wait.until(EC.presence_of_element_located((by, value)))

def parse_player_info(driver, player_li, soup):
    player_info = player_li.find('div', class_='mu-item__info')
    if player_info:
        team_tag = soup.find('div', class_='main-container').find('h1', class_='screenreader')
        jersey_number_tag = player_info.find('p', class_='mu-item__jersey-number')
        first_name_tag = player_info.find('span', class_='mu-item__firstname')
        last_name_tag = player_info.find('span', class_='mu-item__lastname')
        player_link_tag = player_li.find('a')
        player_link = player_link_tag['href'] if player_link_tag else '#'
        
        driver.get(player_link)
        wait_for_page_to_load(driver, By.CLASS_NAME, 'player-detail-container')
        player_detail = BeautifulSoup(driver.page_source, 'html.parser')
        biography_tag = player_detail.find('div', class_='player-content__inner').find('p')
        biography = biography_tag.text.strip() if biography_tag else 'N/A'

        # Extract position, country, and date of birth
        player_history = player_detail.find('div', class_='player-history')
        
        position_tag = player_history.find('span', string='Position') if player_history else None
        position = position_tag.find_next('p').text.strip() if position_tag else 'N/A'
        
        country_tag = player_history.find('span', string='Country') if player_history else None
        country = country_tag.find_next('p').text.strip() if country_tag else 'N/A'
        
        dob_tag = player_history.find('span', string='Date of birth') if player_history else None
        date_of_birth = dob_tag.find_next('p').text.strip() if dob_tag else 'N/A'

        full_name = f"{first_name_tag.text.strip()} {last_name_tag.text.strip()}" if first_name_tag and last_name_tag else 'N/A'
        team = team_tag.text.strip() if team_tag else 'N/A'
        jersey_number = jersey_number_tag.text.strip() if jersey_number_tag else 'N/A'
        first_name = first_name_tag.text.strip() if first_name_tag else 'N/A'
        last_name = last_name_tag.text.strip() if last_name_tag else 'N/A'

        return {
            'Team': team,
            'Position': position,
            'Jersey Number': jersey_number,
            'First Name': first_name,
            'Last Name': last_name,
            'Full Name': full_name,
            'Link': player_link,
            'Biography': biography,
            'Country': country,
            'Birth': date_of_birth,
        }
    return None

def scrape_players_from_url(driver, url):
    start_url_time = time.time()
    print(f"Scraping URL dimulai: {url} pada {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_url_time))}")

    driver.get(url)
    wait_for_page_to_load(driver, By.CLASS_NAME, 'team-grid__item')

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    team_grid_items = soup.find_all('div', class_='team-grid__item')
    
    players = []

    for team_grid_item in team_grid_items:

        player_lis = team_grid_item.find_all('li', class_='grid-3 teamgrid-ratio')
        for player_li in player_lis:
            player_info = parse_player_info(driver, player_li, soup)
            if player_info:
                players.append(player_info)
    
    end_url_time = time.time()
    print(f"Scraping URL selesai: {url} pada {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_url_time))}")
    print(f"Waktu yang dihabiskan untuk {url}: {end_url_time - start_url_time} detik")
    
    return players

def save_to_csv(filename, data):
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print(f"Data telah disimpan ke file {filename}")

def save_to_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data telah disimpan ke file {filename}")

def main():
    start_time = time.time()
    print("Scraping dimulai pada:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))

    urls = [
        'https://www.manutd.com/en/players-and-staff/first-team',
        'https://www.manutd.com/en/players-and-staff/women',
        'https://www.manutd.com/en/players-and-staff/reserves',
        'https://www.manutd.com/en/players-and-staff/the-academy',
        'https://www.manutd.com/en/players-and-staff/legends'
    ]
    
    driver = setup_driver()
    
    all_players = []
    for url in urls:
        players = scrape_players_from_url(driver, url)
        all_players.extend(players)
    
    driver.quit()

    if all_players:
        save_to_csv('mu_team.csv', all_players)
        save_to_json('mu_team.json', all_players)

    end_time = time.time()
    print("Scraping selesai pada:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print("Total waktu scraping:", end_time - start_time, "detik")

if __name__ == "__main__":
    main()
