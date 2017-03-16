function redirectToLogin() {
    window.location.replace("/login/?next=" + window.location.pathname)
}

function commentAnswer(json) {
    if (json.hasOwnProperty("ok")) {
        $("#comment_form textarea").val("");
        jQuery.each(json.comments, function(index, comment) {
            $("#comments").append(
                        '<div name="comment">' +
                            '<div class="w3-container grey darken-4" style="width:60%">' +
                                '<img class="w3-margin-top w3-margin-right" src="' + comment.author_image_url + '"' +
                                'style="height:50px"/>' +
                                '<font size="+3">' + comment.author + '</font>' +
                                '<font size="-3">' + comment.created_date + '</font>' +
                                '<li class="divider"></li>' +
                                '<p>' + comment.text + '</p>' +
                            '</div>' +
                        '</div>');
            });
    } else {
        redirectToLogin()
    }
}

function addComment(e) {
    e.preventDefault();
    number_of_comments = $("div[name=comment").length;
    $.ajax({
      type: 'post',
      url: ($(e.target).attr("action") + "comments-count/" + number_of_comments + "/ajax/"),
      data: $(e.target).serialize(),
      success: commentAnswer,
    });
}

function voteAnswer(json) {
    if (json.hasOwnProperty("ok")) {
        $("#up_votes").text(json.up_votes);
        $("#down_votes").text(json.down_votes);
    } else {
        redirectToLogin()
    }
}

function vote(e) {
    e.preventDefault();
    $.ajax({
      type: 'post',
      url: ($(e.target).attr("action") + "ajax/"),
      data: $(e.target).serialize(),
      success: voteAnswer,
    });
}

function init() {
	$("#comment_form").submit(addComment);
	$("#up_vote_form").submit(vote);
	$("#down_vote_form").submit(vote);
}

$(document).ready(init);