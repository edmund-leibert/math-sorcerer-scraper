<details>
  <summary>Data Garage Branching Guidelines</summary>

Conventional Commit is a formatting convention that provides a set of rules to formulate a consistent commit message structure like so:

```
<type>[optional scope]: <description>
[optional body]
[optional footer(s)]
```

Commit types include the following...
- `feat` – a new feature is introduced with the changes
- `fix` – a bug fix has occurred
- `chore` – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
- `refactor` – refactored code that neither fixes a bug nor adds a feature
- `docs` – updates to documentation such as a the README or other markdown files
- `style` – changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
- `test` – including new or correcting previous tests
- `perf` – performance improvements
- `ci` – continuous integration related
- `build` – changes that affect the build system or external dependencies
- `revert` – reverts a previous commit
  
| Gitmojis                                  |   |                                                          |   |                                          |   |                                                                 |   |
|-------------------------------------------|---|----------------------------------------------------------|---|------------------------------------------|---|-----------------------------------------------------------------|---|
| 🎨 Improve structure / format of the code. |   | 📌 Pin dependencies to specific versions.                 |   | ♿ Improve accessibility.                 |   | 🚩 Add, update, or remove feature flags.                         |   |
| ⚡ Improve performance.                    |   | 👷 Add or update CI build system.                         |   | 💡 Add or update comments in source code. |   | 🥅 Catch errors.                                                 |   |
| 🔥 Remove code or files.                   |   | 📈 Add or update analytics or track code.                 |   | 🍻 Write code drunkenly.                  |   | 💫 Add or update animations and transitions.                     |   |
| 🐛 Fix a bug.                              |   | ♻️ Refactor code.                                         |   | 💬 Add or update text and literals.       |   | 🗑️ Deprecate code that needs to be cleaned up.                   |   |
| 🚑 Critical hotfix.                        |   | ➕ Add a dependency.                                      |   | 🗃️ Perform database related changes.      |   | 🛂 Work on code related to authorization, roles and permissions. |   |
| ✨ Introduce new features.                 |   | ➖ Remove a dependency.                                   |   | 🔊 Add or update logs.                    |   | 🩹 Simple fix for a non-critical issue.                          |   |
| 📝 Add or update documentation.            |   | 🔧 Add or update configuration files.                     |   | 🔇 Remove logs.                           |   | 🧐 Data exploration/inspection.                                  |   |
| 🚀 Deploy stuff.                           |   | 🔨 Add or update development scripts.                     |   | 👥 Add or update contributor(s).          |   | ⚰️ Remove dead code.                                             |   |
| 💄 Add or update the UI and style files.   |   | 🌐 Internationalization and localization.                 |   | 🚸 Improve user experience / usability.   |   | 🧪 Add a failing test.                                           |   |
| 🎉 Begin a project.                        |   | ✏️ Fix typos.                                             |   | 🏗️ Make architectural changes.            |   | 👔 Add or update business logic.                                 |   |
| ✅ Add, update, or pass tests.             |   | 💩 Write bad code that needs to be improved.              |   | 📱 Work on responsive design.             |   | 🩺 Add or update healthcheck.                                    |   |
| 🔒 Fix security issues.                    |   | ⏪ Revert changes.                                        |   | 🤡 Mock things.                           |   | 🧱 Infrastructure related changes.                               |   |
| 🔐 Add or update secrets.                  |   | 🔀 Merge branches.                                        |   | 🥚 Add or update an easter egg.           |   | 🧑‍💻 Improve developer experience.                                |   |
| 🔖 Release / Version tags.                 |   | 📦 Add or update compiled files or packages.              |   | 🙈 Add or update a .gitignore file.       |   | 💸 Add sponsorships or money related infrastructure.             |   |
| 🚨 Fix compiler / linter warnings.         |   | 👽 Update code due to external API changes.               |   | 📸 Add or update snapshots.               |   | 🧵 Add or update code related to multithreading or concurrency.  |   |
| 🚧 Work in progress.                       |   | 🚚 Move or rename resources (e.g.: files, paths, routes). |   | ⚗️ Perform experiments.                   |   | 🦺 Add or update code related to validation.                     |   |
| 💚 Fix CI Build.                           |   | 📄 Add or update license.                                 |   | 🔍 Improve SEO.                           |   |                                                                 |   |
| ⬇️ Downgrade dependencies.                 |   | 💥 Introduce breaking changes.                            |   | 🏷️ Add or update types.                   |   |                                                                 |   |
| ⬆️ Upgrade dependencies.                   |   | 🍱 Add or update assets.                                  |   | 🌱 Add or update seed files.              |   |                                                                 |   |
  
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
