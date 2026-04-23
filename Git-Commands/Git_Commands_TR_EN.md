<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f05032,50:e34c26,100:f05032&height=130&section=header" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&duration=3000&pause=800&color=f05032&center=true&vCenter=true&width=760&lines=Git+%26+GitHub+Commands+%F0%9F%93%96;Local+%E2%86%94+Remote+%7C+Branch+%7C+Merge;TR+%2F+EN+%7C+TechProEd+2020" alt="Typing SVG" />

</div>

---

> 🇹🇷 [Türkçe](#-türkçe) &nbsp;|&nbsp; 🇬🇧 [English](#-english)

---

# 🇹🇷 Türkçe

## Git Nedir?

**Git** — Yaptığımız değişiklikleri satır satır kaydeden bir **versiyon kontrol aracıdır**. Bilgisayarımızda (local) kayıt yapar.

**GitHub** — Git ile bilgisayarımıza kaydettiğimiz projeyi **uzak sunucularda (remote)** saklamamıza yarayan bir araçtır.

### GitHub'ın Faydaları
- 🔐 Bilgi güvenliği
- 🤝 Paylaşılabilme (ortak erişim)
- 🔀 Projeleri birleştirebilme
- ⏪ Geriye dönebilme (backup)
- ☁️ Bilgisayara gerek duymadan uzaktan çalışabilme

---

## 🖥️ Temel CMD Komutları

> ⚠️ Bunlar Git komutları **değildir** — günlük terminalde kullanılır!

| Komut | Açıklama |
|-------|----------|
| `cd klasörAdı` | Klasör değiştir |
| `cd ..` | Bir üst klasöre çık |
| `pwd` | Bulunduğun klasörün adresini göster |
| `ls` | Klasördeki dosyaları listele |
| `dir` | Klasördeki dosyaları ayrıntılı göster |
| `cls` | Terminal ekranını temizle |

---

## 📦 Local Repository Komutları

```bash
# 1. Local repo oluştur (her proje için sadece 1 kez!)
git init

# 2. Dosyaları staging area'ya ekle
git add .              # tüm değişiklikleri ekle
git add dosyaAdı.java  # belirli bir dosyayı ekle

# 3. Commit — dosyalara kimlik kazandır
git commit -m "commit mesajın"

# Durum kontrolü (her zaman kullanabilirsin)
git status

# Geçmiş commit'leri gör
git log

# Belirli bir commit'in detaylarını gör
git show commitIdninİlk5Hanesi
```

---

## ☁️ Remote Repository Komutları

```bash
# 4. Local'den Remote'a gönder
git push

# 5. Remote'dan verileri local'e getir (birleştirmez)
git fetch

# 6. Getirilen verileri projeye birleştir
git merge

# 7. fetch + merge tek seferde (en çok kullanılan)
git pull
```

### 📊 Akış Şeması

```
LOCAL                          REMOTE (GitHub)
  │                                  │
  │  git add .                       │
  │──────────────► Staging Area      │
  │                    │             │
  │  git commit -m ""  │             │
  │◄───────────────────┘             │
  │  Local Repo                      │
  │                                  │
  │  git push ──────────────────────►│
  │                                  │
  │◄──────────────────────── git pull│
```

---

## 🌿 Branch (Dal) Komutları

```bash
# Mevcut branch'leri listele (* aktif branch'i gösterir)
git branch

# Yeni branch oluştur
git branch branchAdı

# Başka bir branch'e geç
git checkout branchAdı

# Yeni branch oluştur ve hemen geç
git checkout -b branchAdı

# Branch'i sil
git branch -D branchAdı

# Local branch'i ilk kez remote'a gönder
git push --set-upstream origin branchAdı

# Başka bir branch'i aktif branch'e birleştir
git merge branchAdı
```

> 💡 **NOT:** `git push` sadece `master` branch'i gönderir. Farklı bir branch göndermek için `--set-upstream` kullan!

---

## 🔀 Pull Request (PR) Nedir?

PR = **Kod çekme talebi**

Remote'ta kendi branch'inden master'a bir şey aktarmak istiyorsan PR yapman gerekir.

```
feature branch  ──► Pull Request ──► master branch
```

---

## 🗃️ Stash Komutları

```bash
# Değişiklikleri geçici kaydet, önceki commit'e dön
git stash

# Kaydedilen değişiklikleri geri getir ve birleştir
git stash apply stash@{0}
```

> 💡 `git stash` — yazdığın kodları kaydeder ve son commit'ine geri döner. Acil başka bir şeye geçmen gerektiğinde kullanışlıdır.

---

## 🙈 .gitignore

`.gitignore` dosyası içine yazdığın dosya veya klasörler **Git tarafından takip edilmez**.

```
# .gitignore örneği
*.log
*.class
target/
.env
node_modules/
```

---

## ⚠️ Conflict (Çakışma) Nedir?

Aynı dosyanın aynı satırı **hem local'de hem remote'da** değiştirilmişse conflict oluşur.

```bash
# Conflict'i çözmek için:
# 1. git pull yap
# 2. Çakışan dosyaları elle düzenle
# 3. git add . → git commit → git push
```

---

## 🔄 Tüm Değişiklikleri Sil (Dikkatli Kullan!)

```bash
# Tüm local değişiklikleri sil, remote master'a eşitle
git reset --hard origin/master
```

> ⚠️ **DİKKAT:** Bu komut tüm kaydetmediğin değişiklikleri **kalıcı olarak siler!**

---

## 🔗 Eclipse'e GitHub Projesi Import Etme

```
1. File → Import
2. Git → Projects from Git → Next
3. Clone URI → Next
4. GitHub URL'yi yapıştır (örn: https://github.com/kullanıcı/repo.git)
5. Next → Next → Next
6. Proje sende yoksa → "Import as general project"
   Proje sende varsa   → "Import existing Eclipse projects"
7. Next → Finish
```

---

## 📋 Komut Özeti

| Komut | Ne Yapar? |
|-------|-----------|
| `git init` | Local repo oluştur |
| `git add .` | Tüm değişiklikleri staging'e ekle |
| `git commit -m "mesaj"` | Commit oluştur |
| `git push` | Remote'a gönder |
| `git pull` | Remote'tan al + birleştir |
| `git fetch` | Remote'tan al (birleştirmez) |
| `git merge` | Branch'leri birleştir |
| `git status` | Mevcut durumu göster |
| `git log` | Commit geçmişini göster |
| `git branch` | Branch'leri listele |
| `git branch isim` | Yeni branch oluştur |
| `git checkout isim` | Branch değiştir |
| `git branch -D isim` | Branch sil |
| `git push --set-upstream origin isim` | Branch'i ilk kez remote'a gönder |
| `git stash` | Değişiklikleri geçici kaydet |
| `git stash apply stash@{0}` | Stash'i geri getir |
| `git reset --hard origin/master` | Tüm değişiklikleri sil ⚠️ |

---

---

# 🇬🇧 English

## What is Git?

**Git** — A **version control system** that records changes line by line. It saves data on your local machine.

**GitHub** — A tool for storing Git-tracked projects on **remote servers (cloud)**.

### Benefits of GitHub
- 🔐 Data security
- 🤝 Collaboration (shared access)
- 🔀 Merging projects
- ⏪ Rolling back changes (backup)
- ☁️ Running code remotely without needing your own machine

---

## 🖥️ Basic CMD Commands

> ⚠️ These are **NOT** Git commands — used in everyday terminal!

| Command | Description |
|---------|-------------|
| `cd folderName` | Change directory |
| `cd ..` | Go up one level |
| `pwd` | Print current directory path |
| `ls` | List files in current directory |
| `dir` | List files with details |
| `cls` | Clear the terminal screen |

---

## 📦 Local Repository Commands

```bash
# 1. Initialize local repo (only once per project!)
git init

# 2. Add files to staging area
git add .              # add all changes
git add fileName.java  # add specific file

# 3. Commit — give identity to your changes
git commit -m "your commit message"

# Check current status (use anytime)
git status

# View commit history
git log

# View details of a specific commit
git show first5charsOfCommitId
```

---

## ☁️ Remote Repository Commands

```bash
# 4. Push from local to remote
git push

# 5. Fetch data from remote (doesn't merge)
git fetch

# 6. Merge fetched data into local
git merge

# 7. fetch + merge in one step (most common)
git pull
```

### 📊 Workflow Diagram

```
LOCAL                          REMOTE (GitHub)
  │                                  │
  │  git add .                       │
  │──────────────► Staging Area      │
  │                    │             │
  │  git commit -m ""  │             │
  │◄───────────────────┘             │
  │  Local Repo                      │
  │                                  │
  │  git push ──────────────────────►│
  │                                  │
  │◄──────────────────────── git pull│
```

---

## 🌿 Branch Commands

```bash
# List existing branches (* shows active branch)
git branch

# Create a new branch
git branch branchName

# Switch to another branch
git checkout branchName

# Create and switch to new branch in one step
git checkout -b branchName

# Delete a branch
git branch -D branchName

# Push local branch to remote for the first time
git push --set-upstream origin branchName

# Merge another branch into the current branch
git merge branchName
```

> 💡 **NOTE:** `git push` only pushes the `master` branch. Use `--set-upstream` to push a different branch!

---

## 🔀 What is a Pull Request (PR)?

PR = **Code Pull Request**

If you want to merge changes from your own remote branch into master, you need to open a Pull Request.

```
feature branch  ──► Pull Request ──► master branch
```

---

## 🗃️ Stash Commands

```bash
# Temporarily save changes and return to last commit
git stash

# Restore saved changes and merge
git stash apply stash@{0}
```

> 💡 `git stash` — saves your current code and returns to the previous commit. Useful when you need to urgently switch to something else.

---

## 🙈 .gitignore

Files or folders listed in `.gitignore` are **ignored by Git**.

```
# .gitignore example
*.log
*.class
target/
.env
node_modules/
```

---

## ⚠️ What is a Conflict?

A conflict occurs when the **same line of the same file** is changed both **locally and remotely**.

```bash
# To resolve a conflict:
# 1. Run git pull
# 2. Manually edit the conflicting files
# 3. git add . → git commit → git push
```

---

## 🔄 Reset All Changes (Use with Caution!)

```bash
# Discard all local changes, sync with remote master
git reset --hard origin/master
```

> ⚠️ **WARNING:** This command **permanently deletes** all unsaved changes!

---

## 🔗 Importing a GitHub Project into Eclipse

```
1. File → Import
2. Git → Projects from Git → Next
3. Clone URI → Next
4. Paste the GitHub URL (e.g. https://github.com/user/repo.git)
5. Next → Next → Next
6. If project doesn't exist locally → "Import as general project"
   If project already exists locally → "Import existing Eclipse projects"
7. Next → Finish
```

---

## 📋 Command Summary

| Command | What it does |
|---------|-------------|
| `git init` | Initialize local repo |
| `git add .` | Add all changes to staging |
| `git commit -m "msg"` | Create a commit |
| `git push` | Send to remote |
| `git pull` | Get from remote + merge |
| `git fetch` | Get from remote (no merge) |
| `git merge` | Merge branches |
| `git status` | Show current status |
| `git log` | Show commit history |
| `git branch` | List branches |
| `git branch name` | Create new branch |
| `git checkout name` | Switch branch |
| `git branch -D name` | Delete branch |
| `git push --set-upstream origin name` | Push branch to remote for first time |
| `git stash` | Temporarily save changes |
| `git stash apply stash@{0}` | Restore stashed changes |
| `git reset --hard origin/master` | Discard all changes ⚠️ |

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f05032,50:e34c26,100:f05032&height=80&section=footer" width="100%"/>

**Gamzenur Uzunlu** · [github.com/pinhanderler](https://github.com/pinhanderler)

</div>
