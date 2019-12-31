if [ $# -eq 0 ]
	then
		MSG = $1
	else
		MSG = "Trigger Re-Deploy"
fi

git add .
git commit --allow-empty -m MSG
git push heroku flask-hero-api:master

