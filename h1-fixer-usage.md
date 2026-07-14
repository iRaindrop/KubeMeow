# H1 Fixer

**UPDATE:** This fix is moot as the practice of not using H1s is an established practice.

There are currently ~132 Flatcar topics that are missing their H1 headings, e.g. "# Flatcar Container Linux". The reason these files still build is because the title in the metadata, on line 2 after the opening "---" delimiter, is picked up by the build if there's no H1.

The H1, such as `# Flatcar Container Linux`, should be between the closing delimiter of the metadata and the first line of text, but surrounded by blank lines, like this:

    (metadata)
    ---

    You can use common debugging tools ...

With H1 added:

    (metadata)
    ---

    # Flatcar debugging tools

    You can use common debugging tools ...


The metadata title and the H1 are typically the same, but there are key differences you can take advantage of:

- The metadata title is used by SEO and should contain more words to help identify the topic in searches, such as "Debugging tools on Flatcar Container Linux".
- The H1 title can be shorter and is the title that will appear on the page. If the metadata has linktitle, that's used for navigation - like the on the left-side.

## Run the script

The Python script, `h1-fixer.py` is available in my repo:

https://github.com/iRaindrop/KubeMeow/blob/main/h1-fixer.py

It has two functions that you can run on the command line:

- `find_missing_h1_headings` - No need to run, edit the spreadsheet.
- `add_missing_h1_headings`


### Find Missing H1s

Run the script if needed. The `output-csv` can be named as desired. You can also change `local-path` to target folders.

Usage:

```python

python3 h1-fixer.py find --local-path /home/brucehamilton/github/flatcar-refactor/content/docs/latest --output-csv missing_h1_headings.csv
```

Import the sheet into Google sheets. 


### Edit the spreadsheet

Here's the google sheet of the missing H1s. Ownership is being transferred to Jan.

https://docs.google.com/spreadsheets/d/18sHX2hkL-ulZv7uPYlUDnWGo-XqhzCuuzqOdcMEEH2o/edit?usp=sharing

It has these columns: `path`, `filename`, `meta-title`, and `new-h1`.

The `meta-title` column contains the tiles from the metadata and the `new-h1` column has the metadata titles that I copied into it. Edit the sheet to have the titles and H1s you want.

Then download the sheet to a CSV, such as `add-h1-headings.csv`. You can break the job into chunks by downloading selected rows that are copied into another sheet.

### Add/Update H1s and titles

After downloading the CSV, run the script to update the files.

For each file in the csv, the script will add the H1 heading with the value from the `new-h1` column. If the `meta-title` is different than what's currently in the file's metadata, the script will update the metadata title with the value from the `meta-title`column.

The script will not add the H1 if by chance the H1 is already present. 

```python

python3 h1-fixer.py add --local-path /home/brucehamilton/github/flatcar-refactor/content/docs/latest --input-csv add-h1-headings.csv
```


