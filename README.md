# why...

## Instructions:

Close all Chrome instances and open your terminal.  

For macOS, enter this command:  
```sh
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

For Windows, enter this command:  
```sh
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

For Linux, enter this command:  
```sh
google-chrome --remote-debugging-port=9222
```

Once a Chrome window is launched, run:  
```sh
python main.py
```

Enter the URL in the terminal in response to the `"Enter URL"` prompt.  

Make sure you've already clicked through the prompt for new visitors to the site, or else the clicking won't work. You can also click through it during the 5 second window before the clicking starts.

To stop the automation, just terminate the program with:  
```sh
Ctrl+C
```

At the end, don't forget to close the Chrome instance that was opened with remote debugging.
