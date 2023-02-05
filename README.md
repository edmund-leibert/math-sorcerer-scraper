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

    %% Update the math sorcerer database
    id8["update math sorcerer database"]
    id9["run request on the following url...  <a href='http://google.com'>link</a> and store into variable called <b>response</b>"]
    id10["use BeautifulSoup, with lxml, to parse the <b>response.content</b> variable and store into a variable named soup"]

    %% requests
    %% bs4
    %% pandas

    idStart-->id1-->id2-->id3-->id4-->id5-->id6-->id7
    id7-->id8-->id9-->id10-->id7
    id7-->idEnd
    
```

 ```mermaid 
 %%{init: { 'theme':'forest', 'sequence': {'useMaxWidth':false} } }%%
 sequenceDiagram 
   alice ->> mark: Sent a flower
 ```
