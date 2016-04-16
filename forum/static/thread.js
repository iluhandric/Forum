$(document).ready(
            function () {
                $('[data-toggle="tooltip"]').tooltip();
                $.fn.updateCounter = function (){
                    $.getJSON("/api/counter.json?pk=" + pk).done(function(json){
                        $("#counter").html("People viewing: " + json["count"])
                    });
                };
                var current_page = 0;
                $.fn.updateCounter();
                setInterval(function() {
                    $.fn.updateCounter();
                }, 5000);
                $.fn.reloadComments = function() {
                    $.getJSON("/api/comments.json?pk=" + pk).done(
                        function(response) {
                            var comments = JSON.parse(response);
                            $t = $("#comments-settion");
                            $t.html("");
                            if ((current_page + 1) * 10 < comments.length){
                                $('#older-div-top').html('Older&nbsp  <i class="fa fa-chevron-right" aria-hidden="true" style="font-size: xx-large; float: right"></i>');
                            } else {
                                $('#older-div-top').html("")
                            }
                            if (current_page > 0){
                                $('#newer-div-top').html('<i class="fa fa-chevron-left" aria-hidden="true" style="font-size: xx-large; float: left"></i> &nbspNewer');
                            } else {
                                $('#newer-div-top').html("")
                            }
                            if ((current_page + 1) * 10 < comments.length){
                                $('#older-div-bottom').html('Older&nbsp  <i class="fa fa-chevron-right" aria-hidden="true" style="font-size: xx-large; float: right"></i>');
                            } else {
                                $('#older-div-bottom').html("")
                            }
                            if (current_page > 0){
                                $('#newer-div-bottom').html('<i class="fa fa-chevron-left" aria-hidden="true" style="font-size: xx-large; float: left"></i> &nbspNewer');
                            } else {
                                $('#newer-div-bottom').html("")
                            }
                            if (comments.length > 1) {
                                $t.append('<h1 align="center" style=" font-size: large" >' + (current_page*10 + 1) + " - " +
                                    Math.min(comments.length, 10*(current_page+1)) + '  of ' +
                                        comments.length + " Comments </h1>");
                            } else {
                                if (comments.length == 1) {
                                    $t.append('<h1 align="center" style=" font-size: xx-large" >' +
                                            1 + " Comment </h1>");
                                } else {
                                    $t.append('<h1 align="center" style=" font-size: xx-large" >No comments yet</h1>');

                                }
                            }
                            for (var i = 10*current_page; i != Math.min(comments.length, 10*(current_page+1)); ++i) {
                                var comment_body = '';
                                var text = comments[i].text;
                                text = text.replace('<', '&lt;').replace('>', '&gt;');
                                if (comments[i].image > '0') {
                                    image_url = '/media/' + comments[i].image;
                                    comment_body = '<div style="background-color: #eaeaea; padding: 10px; margin: 10px"> <div align="right" style="font-size: x-small; color: #aaaaaa">' + comments[i].time_posted + "</div>" + '<img align="center" style = "width: auto; max-width: 50%; height:auto" src =' + image_url + '>' + '<h1 style="font-size: medium; word-break: break-all " >' + text + '</h1></div>'

                                } else {

                                    comment_body = '<div style="background-color: #eaeaea; padding: 10px; margin: 10px"> <div align="right" style="font-size: x-small; color: #aaaaaa">' + comments[i].time_posted + "</div>" + '<h1 style="font-size: medium; word-break: break-all " >' + text + '</h1></div>'
                                }
                                $t.append(comment_body);
                            }
                        }
                    );
                };
                $.fn.reloadComments();
                $("#reload").click(function() {
                    $.fn.reloadComments()
                });
                $("#older-div-top").click(function() {
                    current_page++;
                    $.fn.reloadComments()
                });
                $("#newer-div-top").click(function() {
                    current_page--;
                    $.fn.reloadComments()
                });
                $("#older-div-bottom").click(function() {
                    current_page++;
                    $.fn.reloadComments()
                });
                $("#newer-div-bottom").click(function() {
                    current_page--;
                    $.fn.reloadComments()
                });
            }
        );

