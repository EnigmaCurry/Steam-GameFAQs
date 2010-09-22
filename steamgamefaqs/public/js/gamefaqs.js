var results = $(null);
var current_result = 0;
var previous_page_term = null;
var toolbar_margin = 75;

function get_page(url) {
  $.ajax({url: "/gamefaqs/get_remote_page?url="+url,
          dataType: "html",
          success: function(data) {
            vdata = data;
            var faq = $(data).find("pre");
            $("div#contents").html(faq);
            $("body").stop().scrollTop(0);
          }});
}
            
function hide_results() {
  $("div#contents").removeHighlight();
  $(".search-results").hide();
}

function scroll_result() {
  //Scroll to the current result
  $("#num-results").html((current_result+1)+" of "+(results.length));
  var r = results[current_result];
  if(r) {
    //Animated scrolling is cool, but the steam browser sucks :(
    //$("body").stop().animate({scrollTop: r.offsetTop - toolbar_margin})
    $("body").stop().scrollTop(r.offsetTop - toolbar_margin);
    //Highlight the current result differently
    results.removeClass("current_result");
    $(r).addClass("current_result");
  }
}

  

function next_result() {
  if (current_result > -1) { 
    if (current_result < results.length - 1) {
      current_result += 1;
    } else {
      current_result = 0;
    }
    scroll_result();
  }
}

function prev_result() {
  if (current_result > -1) {
    if (current_result > 0) {
      current_result -= 1;
    } else {
      current_result = results.length - 1;
    }
    scroll_result();
  }
}

function search_page(term) {
  $(".search-results").show();
  $("div#contents").removeHighlight().highlight(term);
  results = $("span.highlight");
  if (results.length >= 1) {
    current_result = 0;
  } else {
    current_result = -1;
  }
  scroll_result();
}


function search_page_as_typed() {
  var val = $.trim($("input#search-page").val());
  if (val.length == 0) {
    hide_results();
  } else {
    search_page(val);
  }   
}

function search_games(name) {
  $.getJSON("/gamefaqs/search_games?name="+name, function(data) {
    var page = $("div#contents");
    var src = "";
    var games = data['games'];
    src+="<div id='game-results'>\n";
    src+="<h3>Games</h3>\n";
    src+="<table>\n";
    src+="<tr><th>Name</th><th>Platform</th></tr>\n";
    for(var i in games) {
        src+="<tr><td><a href='javascript:search_faqs(\""+games[i].url+"\")'>"+games[i].title+"</a></td><td>"+games[i].platform+"</td></tr>\n"
    }
    src+="</table>\n";
    src+="</div>\n";
    page.html(src);
    $("body").stop().scrollTop(0);
  });
}

function search_faqs(game_url) {
  $.getJSON("/gamefaqs/search_faqs?game_url="+game_url, function(data) {
    var page = $("div#contents");
    var src = "";
    var faqs = data['faqs'];
    src+="<div id='game-results'>\n";
    src+="<h3>FAQs</h3>\n";
    src+="<table>\n";
    src+="<tr><th>Name</th><th>Date</th><th>Author</th><th>Version</th><th>Size</th></tr>\n";
    for(var i in faqs) {
        src+="<tr><td><a href='javascript:get_page(\""+faqs[i].url+"\")'>"+faqs[i].title+"</a></td><td>"+faqs[i].date+"</td><td>"+faqs[i].author+"</td><td>"+faqs[i].version+"</td><td>"+faqs[i].size+"</td></tr>\n"
    }
    src+="</table>\n";
    src+="</div>\n";
    page.html(src);
    $("body").stop().scrollTop(0);
  });
}


$(document).ready(function() {
  hide_results();
  $("#ajax-indicator").hide();
  var search_game = $("input#search-games");
  search_game.bind("keyup", function(e) {
    if(e.keyCode == 13) {
      search_games(search_game.val());
      search_game.val("");
    }
  });
  var search_page = $("input#search-page");
  search_page.bind("keyup", function(e) {
    if (e.keyCode == 13) {
      //Enter does two things:
      //Search for the term entered
      //Go to the next match if the term didn't change.
      //This originally was a "search as you type" feature but it
      //proved too resource intensive, especially for the steam browser.
      if(previous_page_term == search_page.val()) {
        next_result();
      } else {
        search_page_as_typed();
        previous_page_term = search_page.val();
      }
      
    }
  });

  //AJAX loading indicator
  $(document).ajaxStart(function() {
    $("#ajax-indicator").show();
  }).ajaxStop(function() {
    $("#ajax-indicator").hide();
  });

  //Next and previous result arrows
  $("#next-result").click(next_result);
  $("#prev-result").click(prev_result);

  //Focus the search in page box when you press Control+F
  $(document).bind("keydown", "ctrl+f", function() {
    $("input#search-page").focus();
  });
});
