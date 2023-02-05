hello

<details>
  <summary>Overview of Math Sorcerer Scraper</summary>

```mermaid

---
title: Data Garage Branching Guidelines
---
  
gitGraph
    commit
    branch "release"
    checkout "main"
    commit
    branch "feature/feature-A"
    commit
    commit
    commit
    checkout "main"
    merge "feature/feature-A"
    branch "feature/feature-B"
    checkout "feature/feature-B"
    commit
    commit
    checkout "main"
    merge "feature/feature-B"
    branch "bugfix/bugfix-A"
    commit
    checkout "main"
    merge "bugfix/bugfix-A"
    checkout "release"
    merge "main"
    checkout "release"
    branch "hotfix/hotfix-A"
    commit
    checkout "release"
    merge "hotfix/hotfix-A"
    checkout "main"
    merge "release"

```
</details>


<style>
  .cssClass > rect {
    fill: #ff0000;
    stroke: #ffff00;
    stroke-width: 4px;
  }
</style>


```mermaid

---
title: Overview of Math Sorcerer Scraper
---

%%{
  init: {
    'theme': 'default',
    'themeVariables': {
      'fontSize': '8px',
      'primaryTextColor': '#000000',
    }
  }
}%%

flowchart TB;
    %% Start and End nodes
    idStart([Start])
    idEnd([End])

    %% Importing modules and other libraries
    id1{{"import the following python libraries... \n &#8226 <b><a href='https://requests.readthedocs.io/en/latest/'>requests</a></b> \n &#8226 <b><a href='https://www.crummy.com/software/BeautifulSoup/'>bs4</a></b> \n &#8226 <b><a href='https://www.pola.rs/'>Polars</a></b> \n &#8226 <b><a href='https://docs.python.org/3/library/os.html'>os</a></b> \n &#8226 <b><a href='https://docs.python.org/3/howto/logging.html'>logging</a></b>"}}

    %% Start program loop
    id2["start program <code>while</code> loop"]

    %% Console menu processes
    id3[/"output to console welcome screen"/]
    id4[/"output to console the following menu selection...\n&#8226 d"/]
    id5[/"request user input"/]
    id6[/"recieve user input"/]
    id7{"what option did\n the user\n select from\n the menu?"}

    %% Scrape the math sorcerer amazon page and update the database
    id8["update math sorcerer database"]
    id9["run request on the url of <a href='https://www.amazon.com/shop/themathsorcerer'>The Math Sorcerer's Lair</a> and store into variable called <pre><code>response</code></pre>"]
    id10["use BeautifulSoup, with lxml, to parse <b>response.content</b> variable and store into a variable named <b>soup</b>"]
    id11["use BeautifulSoup to find all amazon lists in the soup that are related to mathemtics, physics, etc. and store into variable called math_sorcerer_amazon_lists"]
    id12["iterate through math_sorcerer_amazon_lists and call requests on each list"]
    id13["use BeautifulSoup4 to parse through the amazon_list and store all the books in the PostgreSQL database"]
    id14["store the name, edition, etc."]

    %% Print all contents of PostgreSQL database
    id15["access the postgresql database"]
    id16["print all records in the database"]

    %% requests
    %% bs4
    %% pandas

    idStart-->id1-->id2-->id3-->id4-->id5-->id6-->id7
    id7-->id8-->id9-->id10-->id11-->id12-->id13-->id14-->id7
    id7-->id15-->id16-->id7
    id7-->idEnd
```
