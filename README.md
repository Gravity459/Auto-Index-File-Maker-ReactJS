# Automatic `index.js` Generator for Assets and Components

## Overview

This Python script simplifies the organization of your JavaScript/React project by automatically creating `index.js` files for both the "assets" and "components" folders. These `index.js` files serve as entry points for importing assets (e.g., icons, SVGs, images) and components, making it easier to manage and import resources within your project.

## Features

- **Automatic Index Generation**: The script scans the "assets" and "components" folders and generates `index.js` files with import statements for each item found.

- **Customizable**: You can configure the script to include only specific file types (e.g., icons, SVGs, images) or exclude certain files or directories.

- **Organized Imports**: The generated `index.js` files ensure that imports are well-structured and follow best practices, making it easier to maintain your project's structure.

## Usage

1. Clone or download the repository containing the Python script.

2. Navigate to the root directory of your JavaScript/React project.

3. Open a terminal and run the script by executing the following command:

```bash
   python3 generate_index.py
```

1. The script will automatically create index.js files in the "assets" and "components" folders, populating them with import statements for the respective files.

## Configuration
You can customize the script's behavior by modifying the configuration options in the script itself. Some configurable options include:

Take user input (if your assets and components directories are stored other than the path in the script).
File types to include/exclude.
Excluded files or directories.
Output file name (default: `index.js`).

## Example

After running the script, your project directory structure will look like this:

project-root/
   src/
     assets/
       icon1.svg
       icon2.svg
       image1.png
       index.js (automatically generated)
     components/
       Button.js
       Card.js
       Header.js
       index.js (automatically generated)
  generate_index.py


