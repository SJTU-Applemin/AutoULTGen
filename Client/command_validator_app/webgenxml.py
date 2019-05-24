### extract user config from web page, save into xml
import bs4 as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import (
    Element, SubElement, tostring, XML, Comment
)
from ElementTree_pretty import prettify
from prettytable import PrettyTable

def insert_table(trs, validate_group):
    ####-----------------------------------
    ####insert table into tree
    x = PrettyTable()          
    value_name_list = []
    for index, value in enumerate(trs[0].find_elements_by_xpath("./th")):
        if value.text:
            value_name_list.append(value.text.strip())
        else:
            value_name_list.append('')
    x.field_names = value_name_list 

    for name in value_name_list:
        th_group = SubElement(validate_group, 'th')
        th_group.text = name

    for tr in trs[1:]:
        value_list = []
        for index, value in enumerate(tr.find_elements_by_xpath("./td")):
            if value.text:
                value_list.append(value.text.strip())
            else:
                value_list.append('')
        x.add_row(value_list)
      
        for value in value_list:
            td_group = SubElement(validate_group, 'td')
            td_group.text = value

        return x        #print table
    ####-----------------------------------

def webgen(url):
    ##---------------------------------------------------------------------
    # user should put browser driver into working dir
    # Ref: http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php
    browser = webdriver.Chrome()    #replace with .Firefox(), or with the browser of your choice
    #url = "https://gfxspecs.intel.com/Predator/Home/Index/18576"    ##Instruction_FACE_DETECTION， how to find other page by name??
    browser.implicitly_wait(30)
    browser.get(url) #navigate to the page
    #wait a bit till the page is fully loaded
    WebDriverWait(browser, 100).until(EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_xpath("//iframe[@class='ContentIFrame']")))
    WebDriverWait(browser, 200).until(EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_xpath("//iframe[@class='InfiniteScrollPageFrame']")))   ##the first one
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
    ##extract table from innerHtml
    soup = bs.BeautifulSoup(innerHTML,'lxml')
    #print(soup.prettify())
    with open( 'output.xml', "w") as f:
            f.write(soup.prettify())
    ##---------------------------------------------------------------------

    ##---------------------------------------------------------------------
    # generate xml from web page
    TestName = Element('TestName')
    comment = Comment('This is cmd configure web page')
    TestName.append(comment)
    ##---------------------------------------------------------------------

    ##---------------------------------------------------------------------
    ##read specific element
    for dword in browser.find_elements_by_xpath("//div[starts-with(normalize-space(text()),  'DWord')]"):
        dword_group = SubElement(TestName, 'DWord')
        dword_group.set('value', dword.text.split(':')[-1].strip())
        #if dword_group.attrib['value'] == '0':
        for bitfield in dword.find_elements_by_xpath("./following-sibling::table//div[starts-with(normalize-space(text()), 'BitField')]"):
            bitfield_group = SubElement(dword_group, 'bitfield')
            bitfield_group.set('name',  bitfield.text.split(':')[-1].strip())
            bitfield_addr = bitfield.find_elements_by_xpath("./following-sibling::table[@class='WithSidebar']//td[@class='Sidebar']//div[@class='Value Bits']")
            if bitfield_addr:
                bitfield_group.set('addr',  bitfield_addr[0].text.strip())
            validate_values = bitfield.find_elements_by_xpath("./following-sibling::table[@class='WithSidebar']//table[@class='ValidValues']/tbody")
            if validate_values:
                validate_group = SubElement(bitfield_group, 'table')
                validate_group.set('class', 'ValidValues')
                for value in validate_values:
                    trs = value.find_elements_by_xpath("./tr")
                    print(insert_table(trs, validate_group))

    print(prettify(TestName))

if __name__ == '__main__':
    url = ''
    webgen(url)


##---------------------------------------------------------------------

