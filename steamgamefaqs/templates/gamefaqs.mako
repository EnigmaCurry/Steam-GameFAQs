<html>
  <head>
    <link rel="stylesheet" type="text/css" href="/css/gamefaqs.css"/>
    
    <script language="javascript" type="text/javascript" 
            src="/js/jquery-1.4.2.min.js"></script>
    <script language="javascript" type="text/javascript" 
            src="/js/highlight.js"></script>
    <script language="javascript" type="text/javascript" 
            src="/js/jquery.hotkeys.js"></script>
    <script language="javascript" type="text/javascript"
            src="/js/gamefaqs.js"></script>
  </head>
  <body>
    <div id="toolbar">
      <div id="title">SteamFAQs
      <br/>
      <img src="/img/loading.gif" id="ajax-indicator"/>
      </div>
      <div id="search">
        <table>
          <tr>
            <th>Search Games</th>
            <th>Search this Page</th>
            <th><span class="search-results">Search Results</span></th>
          </tr>
          <tr>
            <td>
              <input type="text" name="search-games" id="search-games"/>
            </td>
            <td>
              <input type="text" name="search-page" id="search-page"/>
            </td>
            <td class="search-results">
              <table>
                <tr>
                  <td id="prev-result">&#x2191;</td>
                  <td id="next-result">&#x2193;</td>
                  <td id="num-results"></td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </div>
    </div>
    <div id="contents">
    </div>
  </body>
</html>
