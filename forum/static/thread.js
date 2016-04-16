$(document).ready(
            function () {
                $('[data-toggle="tooltip"]').tooltip();
                $.fn.updateCounter = function (){
                    $.getJSON("/api/counter.json?pk=" + pk).done(function(json){
                        $("#counter").html("People viewing: " + json["count"])
                    });
                };
                $.fn.updateCounter();
                setInterval(function() {
                    $.fn.updateCounter();
                }, 5000);
                $.fn.reloadComments = function() {
                    $.getJSON("/api/comments.json?pk=" + pk).done(
                        function(response) {
                            var comments = JSON.parse(response);
                            $t = $("#here");
                            $t.html("");
                            if (comments.length > 1) {
                                $t.append('<h1 align="center" style=" font-size: large" >' +
                                        comments.length + " Comments </h1>");
                            } else {
                                if (comments.length == 1) {
                                    $t.append('<h1 align="center" style=" font-size: xx-large" >' +
                                            1 + " Comment </h1>");
                                } else {
                                    $t.append('<h1 align="center" style=" font-size: xx-large" >No comments yet</h1>');

                                }
                            }
                            for (var i = 0; i != comments.length; ++i) {
                                var comment_body = '';
                                if (comments[i].image > '0') {
                                    image_url = '/media/' + comments[i].image;
                                    comment_body = '<div style="background-color: #eaeaea; padding: 10px; margin: 10px"> <div align="right" style="font-size: x-small; color: #aaaaaa">' + comments[i].time_posted + "</div>" + '<img align="center" style = "width: auto; max-width: 50%; height:auto" src =' + image_url + '>' + '<h1 style="font-size: medium; word-break: break-all " >' + comments[i].text + '</h1></div>'

                                } else {
                                    comment_body = '<div style="background-color: #eaeaea; padding: 10px; margin: 10px"> <div align="right" style="font-size: x-small; color: #aaaaaa">' + comments[i].time_posted + "</div>" + '<h1 style="font-size: medium; word-break: break-all " >' + comments[i].text + '</h1></div>'
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
            }
        );

