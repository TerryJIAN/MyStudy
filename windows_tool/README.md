# windows_tool
<h6>del.bat
<p>DEL /F /A /Q \\?\%1
<p>RD /S /Q \\?\%1

看到上面那兩行，對於經歷過 DOS 時代的人應該很熟悉，其意思分別為刪除檔案（DEL、ERASE）與刪除資料夾（RD、RMDIR），而％1是代表傳入的參數。

DEL 刪除檔案，命令參數： del /?
/F：表示強制刪除
/A：選擇檔案的屬性
/Q：安靜模式，不會跳出提示訊息就刪除
/S：連帶刪除子目錄下的檔案

RD 刪除目錄，命令參數： rd /?
/Q：安靜模式，不會跳出 提示訊息就刪除
/S：連帶刪除子目錄下的檔案

--------怎麼使用呢？-------

方法很簡單，就是將上面兩行存到一個文字檔案，並且更名為 xx.bat （Batch File）

然後將你無法刪除的檔案或目錄拉到該 BAT 檔，咻一下就刪除了

很簡單、很方便、處理方式很透明～贊......有被鎖檔的朋友不妨試試看這個方法。

--------開機執行方法--------

1.可以使用"工作排程器" 記得勾選最高管理員執行(在下方 仔細找)!!

2.放置在該目錄下=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\啟動

-----IIS CMD指令創建站點-----

加入:
C:\Windows\system32\inetsrv\appcmd.exe add app /site.name:"Default Web Site" /path:/APP1 /physicalPath:C:\inetpub\wwwroot\APP1

設定:
C:\Windows\system32\inetsrv\appcmd.exe set app "Default Web Site/APP1" /applicationPool:".NET v4.5"

查看website 
C:\Windows\System32\inetsrv\appcmd.exe list app

查看apppool 
C:\Windows\System32\inetsrv\appcmd.exe list apppool

也可改用
%systemroot%\system32\inetsrv\appcmd.exe 或是 %windir%\system32\inetsrv\appcmd.exe
