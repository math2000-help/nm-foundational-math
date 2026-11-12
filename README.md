# Foundational Math Intensive: Workshop Guide Website

This folder is a complete website for the Nuclear Medicine Foundational Math guide (with solutions).
It is built with **Zensical** (the successor to Material for MkDocs) and published for free with **GitHub Pages**.
Math is displayed with **MathJax**.

You do not need to install anything to publish or edit it. Everything below can be done in a web browser.

---

## Part 1: Publish the site (one time, about 15 minutes)

**1. Make a GitHub account.** Go to github.com and sign up (free).

**2. Make a repository.** A repository ("repo") is just an online folder for your files.
Click the **+** at the top right, then **New repository**. Name it something like `nm-foundational-math`.
Choose **Public** (GitHub Pages is free for public repositories), then click **Create repository**.

**3. Unzip this project on your computer.** GitHub cannot take a zip file, so unzip it first.
Important: the folder `.github` is *hidden* on some computers. It is needed for the site to build.
- Mac: in Finder press **Cmd + Shift + .** (period) to show hidden files.
- Windows: in File Explorer choose **View > Show > Hidden items**.

**4. Upload the files.** On your new repo page click **uploading an existing file**.
Select everything inside the unzipped folder (`docs`, `tools`, `.github`, `mkdocs.yml`, `requirements.txt`, `README.md`, `.gitignore`) and drag it into the browser.
Scroll down and click **Commit changes**.

**5. Turn on GitHub Pages.** In your repo click **Settings > Pages**.
Under **Build and deployment > Source**, choose **GitHub Actions**.

**6. Wait about two minutes.** Click the **Actions** tab. When the "Publish site" run shows a green check, your site is live.
The address is `https://YOUR-USERNAME.github.io/nm-foundational-math/`. Share that link with students.

(Optional) Open `mkdocs.yml`, remove the `#` in front of the `site_url` line, and put your real address there.

---

## Part 2: Editing the site later

Every page is a plain text file in the `docs` folder. To change one:

1. In your repo click `docs`, then click the page (for example `topic-06-concentration-volume.md`).
2. Click the **pencil icon** (Edit).
3. Make your change and click **Commit changes**.
4. The site rebuilds by itself in about two minutes.

### How things are written

| You want | Type this |
| --- | --- |
| Bold text | `**bold**` |
| Math in a sentence | `\( C = \dfrac{A}{V} \)` |
| Math on its own line | `\[` then the math on the next line, then `\]` on a line by itself |
| Red cancel marks | `\cancel{\text{mCi}}`, `\bcancel{\text{kg}}`, `\xcancel{\text{lb}}` |
| Worked example box | `!!! example "Ex 1.1"` then indent the contents by 4 spaces |
| Try problem with a hidden answer | see any Try problem in a topic page and copy it |

The easiest way to add a problem is to copy an existing one and change the numbers.

---

## Printing and PDFs

- Every page has a **Print / Save as PDF** button. All "Show answer" boxes open automatically in the printout.
- **Print the Full Guide** (last item in the menu) puts every page on one long page, so students can save the entire guide as a single PDF.
  Tip for students: in the print window turn on **Background graphics** so the colored boxes appear.
- The full-guide page is rebuilt automatically every time the site publishes, so it never goes out of date.

---

## Good to know

- Students need an internet connection (the math display loads from a free public library, MathJax).
- The site is public. Anyone with the link can read it, including the answers.
- `tools/convert_tex.py` is the script that converted the original LaTeX guide. You do not need it again unless you want to re-convert a revised `.tex` file.
- The configuration file `mkdocs.yml` also works with Material for MkDocs, in case you ever want to switch.

## Preview on your own computer (optional, for later)

```
pip install -r requirements.txt
python tools/make_print_page.py
zensical serve
```

Then open the address it prints (usually http://localhost:8000).
