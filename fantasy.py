import mechanize
import sys
from bs4 import BeautifulSoup as bs
import team

irUrl = 'https://www.fantasybasketballnerd.com/service/injuries/'

def scrapeData(url):
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    print("Scraping " + url)
    response = br.open(url)
    print("Scraping Complete")
    print("Preparing Data...\n")
    data = response.read()
    return data

def parseXMLForTeam(xmlFile):
    soup = bs(xmlFile,'lxml')
    players = soup.find_all('player')
    for player in players:
        if player.contents[1].getText() in team.playerArr:
            print('Player Name: ' + player.contents[1].getText())
            print('Injury: ' + player.contents[2].getText())
            print('Notes: ' + player.contents[3].getText())
            print('Last Updated: ' + player.contents[4].getText() + '\n')

def parseXMLForPlayer(xmlFile, playerName):
    soup = bs(xmlFile,'lxml')
    players = soup.find_all('player')
    for player in players:
        if player.contents[1].getText() == playerName:
            print('Player Name: ' + player.contents[1].getText())
            print('Injury: ' + player.contents[2].getText())
            print('Notes: ' + player.contents[3].getText())
            print('Last Updated: ' + player.contents[4].getText() + '\n')
            return
    print('--------------------------------')
    print(playerName + ' was not found on the IR.')
    print('--------------------------------\n')

def main():
    if len(sys.argv) > 1:
        data = scrapeData(irUrl)
        playerName = sys.argv[1]
        print('--------------------------------')
        print('Injury Report for: ' + playerName)
        print('--------------------------------\n')
        parseXMLForPlayer(data, playerName)
    else:
        data = scrapeData(irUrl)
        print('--------------------------------')
        print('Fantasy Team Injury Report:')
        print('--------------------------------\n')
        parseXMLForTeam(data)


if __name__ == "__main__":
    main()
