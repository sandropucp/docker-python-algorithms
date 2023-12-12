# Go to local folder
cd LOCALPATH

# Build the image:
docker build . -t python_flask

# Check Docker Images:
docker images

# Run Container with Shared Local Folder in (C:\dev\github\docker-python\src)
docker run -p 5000:5000 -v C:\dev\github\docker-python-algorithms\src:/home/smss6/code -ti --name=python_flask python_flask:latest
python3 app.py
open browser
- [Check Flask is running](http://localhost:5000)
- [Run Fibbonacci](http://localhost:5000/fibbonacci/4)
- [Run LIS](http://localhost:5000/lis/5,7,4,−3,9,1,10,4,5,8,9,3)
- [Run LCS](http://localhost:5000/lcs/BCDBCDA,ABECBAB)
- [Run MSCS](http://localhost:5000/mscs/5,15,-30,10,-5,40,10)
- [Run MPTH](http://localhost:5000/mpth/0,120,160,220,320,420)

# Stop Container
docker stop [IMAGEID]