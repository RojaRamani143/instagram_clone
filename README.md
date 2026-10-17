# InstaVibe — Flask Instagram-inspired Demo

A responsive educational social-media UI with stories, posts, likes, comments, saved posts and follow buttons. **Not affiliated with Instagram.** Uses CSS-generated illustrations, so no missing image files. Interactions are stored in browser localStorage, not a database; this is not a real multi-user social network.

## Folder layout

- `app.py` — Flask server and sample data
- `templates/index.html` — page
- `static/style.css` — responsive styling
- `static/script.js` — browser interactions
- `Dockerfile` — container image
- `Jenkinsfile` — GitHub → Docker → Docker Hub → EC2 deployment

## Run locally on EC2

```bash
cd instagram-clone
docker build -t instagram-image:v1 .
docker run -d --name instagram-container -p 9349:5000 instagram-image:v1
curl http://localhost:9349/health
```

Visit `http://YOUR-EC2-PUBLIC-IP:9349/` after allowing inbound TCP port 9349 from your IP in the EC2 security group.

## Push to GitHub

Create an empty GitHub repository named `instagram-clone` under `RojaRamani143`. Upload **the contents of this folder** (not the outer folder) to the `main` branch. Alternatively:

```bash
cd instagram-clone
git init
git branch -M main
git add .
git commit -m "Initial InstaVibe app"
git remote add origin https://github.com/RojaRamani143/instagram-clone.git
git push -u origin main
```

## Jenkins setup

1. Install Jenkins Pipeline, Git, and Credentials Binding plugins.
2. Install Docker on the Jenkins agent and grant Jenkins permission to use Docker.
3. Add Jenkins global credential: **Kind** `Username with password`, **ID** `dockerhub`, username `ramaniroja`, password a Docker Hub access token with write permission.
4. Create a Jenkins Pipeline job. Select **Pipeline script from SCM**, Git repository `https://github.com/RojaRamani143/instagram-clone.git`, branch `*/main`, script path `Jenkinsfile`.
5. Ensure `ramaniroja/instagram-clone` can be pushed to on Docker Hub (create the repository if necessary).
6. Run **Build Now**. The pipeline builds an image tagged with the Jenkins build number, pushes it, and starts the app on port 9349.

**Important:** If you already ran `instagram-container` manually, the Jenkins Deploy stage will remove and replace that container. Port 9349 must be free. For this practice project, a deployment briefly stops the old container before starting the new one.
