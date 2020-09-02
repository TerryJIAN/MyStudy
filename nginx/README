1.把想寫入規則的設定檔(XXX.conf)放入Nginx container裡面conf.d資料夾 
例如    
volumes:
  - ./conf.d:/etc/nginx/conf.d
2.XXX.conf設定reverse proxy
*******************************XXX.conf*************************************
server {
    listen 80;
    listen [::]:80;
    server_name mysite;
    
    location /myapp/ {
        proxy_pass http://myapp/;
        proxy_http_version 1.1;
        proxy_set_header   Upgrade $http_upgrade;
        proxy_set_header   Connection keep-alive;
        proxy_set_header   Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header   X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;    
       }
	
 
}
*****************************************************************************
