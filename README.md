# 🐘 Masto Maltego Transform

<img width=77 src="https://github.com/user-attachments/assets/a784d63c-59e1-4dbe-b9fe-5393e744a48b">

A **Maltego transform** for [Masto OSINT Tool](https://github.com/C3n7ral051nt4g3ncy/Masto) 🕵️‍♂️, allowing Mastodon username searches across **Mastodon API** and the Masto **Fediverse instance list**.


```
📦 masto_maltego_transform
 ┣ 📜 README.md
 ┣ 📜 LICENSE
 ┣ 📜 requirements.txt
 ┣ 📜 settings.py
 ┣ 📜 project.py
 ┣ 📜 extensions.py
 ┣ 📜 .gitignore
 ┣ 📂 transforms
 ┃ ┣ 📜 MastoUsernameSearch.py
   ┣ 📜 __init__.py
```



---

### **📂 Repository Structure**

🚀 **Masto Maltego Transform** allows you to search Mastodon usernames across **Mastodon API** and the **Masto OSINT Tool Fediverse instance list on**. It returns **profile URLs, extra websites found within the bio and profiles, and federated instances** directly in **Maltego**.

## **⚡ Features**
✅ **Searches the Mastodon API** for usernames.  
✅ **Searches across Fediverse instances** (`fediverse_instances.json`).  
✅ **Extracts extra links** like blogs, sites, and avatar links.  
✅ **Adds results as Maltego entities.**  

---

## **📦 Installation & Setup**


### **1️⃣ Install Dependencies**
```bash
git clone https://github.com/C3n7ral051nt4g3ncy/Masto_Maltego_Transform.git
cd masto_maltego_transform
pip install -r requirements.txt
```


### **2️⃣ Install Maltego TRX**
It should have installed correctly via step 1, but just to make sure: 
```bash
pip install maltego-trx
```


###  **3️⃣ Run the Transform Server**
🚀 Start the local transform server:
```bash
python project.py runserver
```
**Leave this running while using Maltego.**

---

## 🔧 Maltego Configuration
- Open Maltego
- Go to ```Transforms``` → ```New Local Transform```
- Display Name: ```Masto```
- Description: ```Username search on Mastodon instances using Masto OSINT Tool```
- Transform ID: ```maltego.masto```
- Author: ```@OSINT_Tactical```
- Input Entitytype: ```Alias [maltego.Alias]```
- Transform Set: ```None```

- Command: ```/Library/Frameworks/Python.framework/Versions/3.10/bin/python3``` or type ```which python3``` in your terminal to get the correct path.
- Parameters: ```/Users/user/masto_maltego_transform/transforms/MastoUsernameSearch.py %Value%```
- Working directory: ```/Users/user/masto_maltego_transform/transforms/```

## 📸 Maltego Configuration Screenshots

### Local Transform Setup:
<img width=699 src="https://github.com/user-attachments/assets/909de304-e7c5-4c6e-bdd0-a7a9ba876aea"/>

<br>
<br>

### Running the Transform:
<img width=699 src="https://github.com/user-attachments/assets/dff19f9c-1f24-49a4-8d53-66ccb101b302"/>


---


## 📜 License
MIT License. Free to use.

---

## 🚀 Author
By: [@C3n7ral051nt4g3ncy](https://github.com/C3n7ral051nt4g3ncy)
<br>
🔗 X: [@OSINT_Tactical](https://x.com/OSINT_Tactical)






