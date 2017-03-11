function comment_answer(json) {
    $("#comment_form textarea").val("");
    jQuery.each(json, function(index, comment) {
        $("#comments").append(
                    '<div name="comment">' +
                        '<span>' + comment.author + '</span>' +
                        '<span>' + comment.created_date + '</span>' +
                        '<textarea disabled>' + comment.text + '</textarea>' +
                    '</div>');
                    });
}

function add_comment(e) {
    e.preventDefault();
    number_of_comments = $("div[name=comment").length;
    $.ajax({
      type: 'post',
      url: ($(e.target).attr("action") + "comments-count/" + number_of_comments + "/ajax"),
      data: $(e.target).serialize(),
      success: comment_answer,
    });
}
var ob;

function vote_answer(json) {
    $("#up_votes").text(json.up_votes);
    $("#down_votes").text(json.down_votes);
}

function vote(e) {
    e.preventDefault();
    $.ajax({
      type: 'post',
      url: ($(e.target).attr("action") + "ajax"),
      data: $(e.target).serialize(),
      success: vote_answer,
    });
}

function init() {
	$("#comment_form").submit(add_comment);
	$("#up_vote_form").submit(vote);
	$("#down_vote_form").submit(vote);
}

$("document").ready(init);