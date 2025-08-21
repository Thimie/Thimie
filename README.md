- 👋 Hi, I’m @Thimie
- 👀 I’m interested in data and visualization
- 🌱 I’m currently learning a lot of things
- 💞️ I’m looking to collaborate on , you let me know.
- 📫 How to reach me i thought github would have private messaging, if not victorthimie@gmail.com
- 😄 Pronouns: me/me
- ⚡ Fun fact: I'm kinda boring.

<!---
Thimie/Thimie is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->

## Margin allocation tool

`allocation_engine.py` distributes available margin based on each holding's safe capacity. The default data lives in `data/positions.csv`.

Run the allocator with the amount of margin you want to deploy:

```bash
python allocation_engine.py 1163.74
```

Use `--positions` to point to a different CSV file.
