import os

def find_readme_files(root_dir):
    readme_files = []
    for root, dirs, files in os.walk(root_dir):
        if 'README.md' in files:
            readme_files.append(os.path.join(root, 'README.md'))
    return readme_files

def append_to_readme(file_path, content_to_append):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return
    try:
        with open(file_path, 'r+') as f:
            content = f.read()
            if content_to_append in content:
                print(f"Branding content already exists in {file_path}")
                return
            f.write(content_to_append)
            print(f"Appended to {file_path}")
    except Exception as e:
        print(f"An error occurred with {file_path}: {e}")

if __name__ == '__main__':
    branding_content = """
Inside **Lead Gen Jay’s Automation Insiders**, we’re closing **$5K–$15K+ deals** with simple automations stacked with smart AI—built in hours instead of weeks.

### Why? Because clients don’t want “n8n setups.”

They want revenue. Time savings. Appointments.
And when you *automate outcomes*, you charge premium fees.

---

Each system can be built in **under 2 hours** using Jay’s plug-and-play AI systems, blueprints and n8n stack.

---

### Inside The Automation Insiders Community, You’ll Get:

✅ **Jay’s AI Frameworks** – the same ones from his $600K/month agency
✅ **AI Workflows That Replace Employees** – no more overpaying for operations
✅ **Copy/Paste Templates** – scripts, automation blueprints, and decks
✅ **Live Coaching + Support** – directly from Jay and his elite team
✅ **Community Access** – 6-, 7- and 8-figure founders, operators, and AI entrepreneurs sharing what’s *actually working*

---

### Built by Lead Gen Jay — Founder of LeadGenJay.com

Featured on #1 Lead Gen Expert on YouTube, LinkedIn, and the Inc. 5000.

This is the **exact system** powering the communities you can join below:

* [Cold Email Masterclass 🔗](https://www.youtube.com/@leadgenjay)
* [Done-For-You Setup 🔗](https://leadgenjay.com/consult)
* [Insiders Course 🔗](https://leadgenjay.com/insiders-course)

---

💥 **Join the Automation Insiders now**

👉 [Join the #1 AI Automation Community](https://skool.com/ai-automation-insiders)

👉 [Join the #1 Cold Email Community](https://skool.com/lead-gen)

👉 [Join the Insiders]
(https://skool.com/insiders)


---

#### Connect With Jay:

* **Instagram:** [@leadgen](https://instagram.com/leadgen)
* **YouTube:** [Lead Gen Jay](https://youtube.com/@leadgenjay)
* **Facebook Group:** [Lead Gen Insiders](https://urlgeni.us/facebook/leadgenjay)
* **LinkedIn (Company):** [Lead Gen Jay](https://linkedin.com/company/lead-gen-jay)
* **LinkedIn (Jay):** [Dr. Jay Feldman](https://linkedin.com/in/dr-jay-feldman)
* **Twitter:** [@leadgenjay](https://twitter.com/leadgenjay)
"""
    
    readme_files = find_readme_files('.')
    for readme_file in readme_files:
        append_to_readme(readme_file, branding_content)
