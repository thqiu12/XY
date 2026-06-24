# デプロイ手順（xy-cloud.org）

株式会社XY 公式サイトは **静的サイト**（ビルド不要）。GitHub Pages + 独自ドメイン `xy-cloud.org` で公開している。

## 構成

- ホスティング: **GitHub Pages**（リポジトリ `thqiu12/XY`、`main` ブランチ / `(root)`）
- 独自ドメイン: **xy-cloud.org**（リポジトリ直下の `CNAME` ファイルで指定）
- DNS 管理: **Squarespace**（旧 Google Domains から移管）
- HTTPS: GitHub Pages が自動発行（Let's Encrypt）

## 1. GitHub Pages 設定（リポジトリ側）

1. リポジトリ `thqiu12/XY` → **Settings** → **Pages**
2. **Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: **main** / フォルダ **/ (root)** → Save
3. **Custom domain**: `xy-cloud.org`（`CNAME` ファイルにより自動入力）→ DNS check が通れば ✅
4. **Enforce HTTPS** にチェック（証明書発行後に有効化可能）

## 2. DNS 設定（Squarespace 側のカスタムレコード）

### A レコード（apex / 名前 `@`）— GitHub Pages の固定 IP、4 件

| Type | 名前 | データ |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |

### CNAME レコード（www）

| Type | 名前 | データ |
|---|---|---|
| CNAME | www | thqiu12.github.io |

### 触らないレコード（メール用・保持）

- `TXT @ v=spf1 include:_spf.google.com ...`（SPF）
- `TXT google._domainkey ...`（DKIM）
- `MX`（あれば）

これらは Google Workspace メール（setsuiken@xy-cloud.org）用。削除するとメールが止まるので残す。

## 3. 更新フロー

```bash
cd /Users/setsuiken/Desktop/工作/XY_site
# ファイルを編集
git add -A
git commit -m "update: ..."
git push origin main
# 1〜2 分で GitHub Pages が自動再ビルド → https://xy-cloud.org に反映
```

## 4. ローカル確認

```bash
cd /Users/setsuiken/Desktop/工作/XY_site
python3 -m http.server 8000
# http://localhost:8000
```

## 5. 確認用コマンド

```bash
# DNS 伝播
dig +short xy-cloud.org A
dig +short www.xy-cloud.org CNAME

# 配信確認
curl -sI https://xy-cloud.org | head -5
curl -s -o /dev/null -w "%{http_code}\n" https://xy-cloud.org/company.html
```

## 別ホスティングへ移す場合

静的ファイル一式（`*.html` / `css/` / `assets/` / `sitemap.xml` / `robots.txt`）を
公開ディレクトリに置くだけで動く（Vercel / Netlify / レンタルサーバー等）。
GitHub Pages 以外に移す場合は `CNAME` ファイルと DNS の A/CNAME を移行先に合わせて変更する。
