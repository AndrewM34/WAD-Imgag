var page, nextPage;
var maxScrollPosition;

function ajaxNextPage(json) {
    $("#next_page_loading").remove();
    if (json.hasOwnProperty("ok")) {
        jQuery.each(json.posts, function(index, post) {
            postsAppend = '<div class="post">' +
            '<a class="image-list-link" href="/post/' + post.hashid + '/">';
            if (post.category == "NSFW") {
                postsAppend += '<img width="100%" height="100%" src="media/default/uploads/nsfw.png"/>';
            } else {
                if (post.is_video) {
                    postsAppend += '<video width="100%" height="100%" autoplay loop muted' +
                    'onclick="this.paused ? this.play() : this.pause();">' +
                    '<source src="' + post.upload_url + '" type="video/mp4"/>' +
                    '</video>';
                } else {
                    postsAppend += '<img width="100%" height="100%" src="' + post.upload_url + '"/>';
                }
            }
            postsAppend += '<div class="point-info gradient-transparent-black transition"></div>' +
            '</a>' +
            '<div class="hover" style="left:15px;">' +
            '<p>' + post.header + '</p>' +
            '</div>' +
            '</div>';
            $("#posts").append(postsAppend);
        });
    if (json.length == 15) {
        $("#next_page").show();
    }
    maxScrollPosition = 0.90 * $(document).height();
    }
}

function loadNextPageYesNoMaybe(e, currentScrollPosition) {
    if ($(e.target).attr("id") == "next_page") {
        e.preventDefault();
        return true;
    }
    return currentScrollPosition >= maxScrollPosition;
}

function getNextPage(e) {
    if (page < nextPage) {
        var currentScrollPosition = $(window).scrollTop() + $(window).height();
        if (loadNextPageYesNoMaybe(e, currentScrollPosition)) {
            page++;
            $("#posts").append('<img id="next_page_loading" src="/static/images/loading/ajax-loader.gif"' +
                                    'class="img-responsive center-block" />');
            $("#previoues_page").remove();
            $("#next_page").hide();
            $.ajax({
              type: 'get',
              url: ($("#next_page").attr("href") + "ajax/"),
              success: ajaxNextPage,
            });
        }
    }
}

function init() {
    $(window).scroll(getNextPage);
    $("#next_page").click(getNextPage);
    maxScrollPosition = 0.90 * $(document).height();
    if (window.location.pathname == "/"
        || window.location.pathname == "/home/"
        || window.location.pathname.startsWith("/category/")) {
        page = 1;
        nextPage = 2;
    } else {
        pathnameSplits = window.location.pathname.split("/");
        jQuery.each(pathnameSplits, function(index, arg) {
            if (arg == "page" && pathnameSplits.length > index + 1) {
                page = parseInt(pathnameSplits[index + 1]);
                nextPage = page + 1;
            }
        });
    }
}

$(document).ready(init);