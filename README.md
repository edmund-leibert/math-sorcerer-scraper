<details>
  <summary>Data Garage Branching Guidelines</summary>
  
:art:
Improve structure / format of the code.

:zap:
Improve performance.

:fire:
Remove code or files.

:bug:
Fix a bug.

:ambulance:
Critical hotfix.

:sparkles:
Introduce new features.

:memo:
Add or update documentation.

:rocket:
Deploy stuff.

:lipstick:
Add or update the UI and style files.

:tada:
Begin a project.

:white_check_mark:
Add, update, or pass tests.

:lock:
Fix security issues.

:closed_lock_with_key:
Add or update secrets.

:bookmark:
Release / Version tags.

:rotating_light:
Fix compiler / linter warnings.

:construction:
Work in progress.

:green_heart:
Fix CI Build.

:arrow_down:
Downgrade dependencies.

:arrow_up:
Upgrade dependencies.

:pushpin:
Pin dependencies to specific versions.

:construction_worker:
Add or update CI build system.

:chart_with_upwards_trend:
Add or update analytics or track code.

:recycle:
Refactor code.

:heavy_plus_sign:
Add a dependency.

:heavy_minus_sign:
Remove a dependency.

:wrench:
Add or update configuration files.

:hammer:
Add or update development scripts.

:globe_with_meridians:
Internationalization and localization.

:pencil2:
Fix typos.

:poop:
Write bad code that needs to be improved.

:rewind:
Revert changes.

:twisted_rightwards_arrows:
Merge branches.

:package:
Add or update compiled files or packages.

:alien:
Update code due to external API changes.

:truck:
Move or rename resources (e.g.: files, paths, routes).

:page_facing_up:
Add or update license.

:boom:
Introduce breaking changes.

:bento:
Add or update assets.

:wheelchair:
Improve accessibility.

:bulb:
Add or update comments in source code.

:beers:
Write code drunkenly.

:speech_balloon:
Add or update text and literals.

:card_file_box:
Perform database related changes.

:loud_sound:
Add or update logs.

:mute:
Remove logs.

:busts_in_silhouette:
Add or update contributor(s).

:children_crossing:
Improve user experience / usability.

:building_construction:
Make architectural changes.

:iphone:
Work on responsive design.

:clown_face:
Mock things.

:egg:
Add or update an easter egg.

:see_no_evil:
Add or update a .gitignore file.

:camera_flash:
Add or update snapshots.

:alembic:
Perform experiments.

:mag:
Improve SEO.

:label:
Add or update types.

:seedling:
Add or update seed files.

:triangular_flag_on_post:
Add, update, or remove feature flags.

:goal_net:
Catch errors.

:dizzy:
Add or update animations and transitions.

:wastebasket:
Deprecate code that needs to be cleaned up.

:passport_control:
Work on code related to authorization, roles and permissions.

:adhesive_bandage:
Simple fix for a non-critical issue.

:monocle_face:
Data exploration/inspection.

:coffin:
Remove dead code.

:test_tube:
Add a failing test.

:necktie:
Add or update business logic.

:stethoscope:
Add or update healthcheck.

:bricks:
Infrastructure related changes.

:technologist:
Improve developer experience.

:money_with_wings:
Add sponsorships or money related infrastructure.

:thread:
Add or update code related to multithreading or concurrency.

:safety_vest:
Add or update code related to validation.
</details>


<details>
  <summary>Data Garage Branching Guidelines</summary>

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

flowchart TB
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
    id9["run request on the url of <a href='https://www.amazon.com/shop/themathsorcerer'>The Math Sorcerer's Lair</a> and store into variable called <code>response</code>"]
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
</details>


<details>
<summary>Database Diagrams</summary>

```mermaid

---
title: Database Diagrams
---

flowchart TB

```
</details>
