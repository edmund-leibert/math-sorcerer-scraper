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

<details>
  <summary>Overview of Math Sorcerer Scraper</summary>

```mermaid

---
title: Overview of Math Sorcerer Scraper
---

%%{
  init: {
    'theme': 'base',
    'themeVariables': {
      'fontSize': '12px',
      'primaryTextColor': '#000000',
    }
  }
}%%

flowchart TB;
    %% Start and End nodes
    idStart([Start]);
    idEnd([End]);

    %% Importing modules and other libraries
    id1{{"import the following python libraries... \n &#8226 requests \n &#8226 bs4 \n &#8226 polars \n &#8226 os \n &#8226 logging"}};

    %% Start program loop
    id2["start program <code>while</code> loop"];

    %% Console menu processes
    id3[/"output to console welcome screen"/];
    id4[/"output to console the following menu selection...\n&#8226 d"/];
    id5[/"request user input"/];
    id6[/"recieve user input"/];
    id7{"what option did\n the user\n select from\n the menu?"};

    %% Update the math sorcerer database
    id8["update math sorcerer database"];
    id9[run request on the following url...  <a href='http://google.com'>link</a> and store into variable called <code>response</code>]
    id10[use BeautifulSoup, with to parse the <code>response.content</code> variable and store into a variable named soup]

    %% requests
    %% bs4
    %% pandas

    idStart-->id1-->id2-->id3-->id4-->id5-->id6-->id7-->id8-->id9-->id10-->idEnd;
    
```
</details>
