var right = document.getElementById('right');
    var left = document.getElementById('left');

    var right_column = document.getElementById('right_column');
    var left_column = document.getElementById('left_column');

    var discuss = document.getElementById('discuss');

    var ask = document.getElementById('ask');
    var in_center = 1;
    var is_expanded = 0;
    var expanding = 0;

    var is_movingf = 0;
    var is_movinge = 0;

    function expand(side) {
        var elem = document.getElementById(side + "_column");
        var another;
        var description;
        if (side == "left") {
            another = document.getElementById("right_column");
            description = document.getElementById("right_black");
        } else {
            another = document.getElementById("left_column");
            description = document.getElementById("left_black");
        }
        var prs = 50;
        var id = setInterval(frame1, 25);
        left.onmouseover = NULL;
        left.onmouseout = NULL;
        right.onmouseover = NULL;
        right.onmouseout = NULL;

        function frame1() {
            if  (is_movingf){}
            else {
                if (prs == 60) {
                    is_movinge = 0;
                    in_center = 0;
                    clearInterval(id);
                    if (side == "right") {
                        right.onmouseout = mouseOutFunction;
                    } else {
                        left.onmouseout = mouseOutFunction;
                    }
                } else {
                    is_movinge = 1;
                    elem.style.zIndex = 2;
                    another.style.zIndex = 0;
                    description.style.zIndex = 1;
                    prs++;
                    elem.style.width = prs + '%';
                    description.style.opacity = (prs - 50)/11;
                    if (side == "left") {
                        another.style.left = prs + '%';
                        another.style.width = 100 - prs + '%';
                    } else {
                        elem.style.left = 100 - prs + '%';
                        another.style.width = 100 - prs + '%';
                    }
                }
            }
        }
    }
    function filch(side) {
        var elem = document.getElementById(side + "_column");
        var another;
        var description;
        if (side == "left") {
            another = document.getElementById("right_column");
            description = document.getElementById("right_black");
        } else {
            another = document.getElementById("left_column");
            description = document.getElementById("left_black");
        }

        var prs = 60;
        var id = setInterval(frame, 25);
        left.onmouseover = NULL;
        left.onmouseout = NULL;
        right.onmouseover = NULL;
        right.onmouseout = NULL;
        function frame() {
            if (is_movinge) {}
            else {
                if (prs == 50) {
                    in_center = 1;
                    is_movingf = 0;
                    clearInterval(id);
                    left.onmouseover = mouseOverFunction;
                    right.onmouseover = mouseOverFunction;
                    description.style.zIndex = 0;
                } else {
                    is_movingf = 1;
                    description.style.opacity = (prs - 50)/11;
                    prs--;
                    elem.style.width = prs + '%';
                    if (side == "left") {
                        another.style.left = prs + '%';
                        another.style.width = 100 - prs + '%';
                    } else {
                        elem.style.left = 100 - prs + '%';
                        another.style.width = 100 - prs + '%';
                    }
                }
            }
        }
    }

    var mouseOverFunction = function () {
         if (is_movinge || is_movingf) {return;}
        if (this == right) {
            ask.style.color = '#fff';
            this.style.color = '#fff';
            expand("right");
        } else {
            discuss.style.color = '#fff';
            this.style.color = '#fff';
            expand("left");
        }
     };
    /*
    function sleep(ms) {
        ms += new Date().getTime();
        while (new Date() < ms){}
    }
    */
    var mouseOutFunction = function () {
        if (is_movingf || (in_center && !is_movinge)) {return;}
        if (this == right) {
            ask.style.color = '#000';
            this.style.color = '#000';
            filch("right");
        } else {
            discuss.style.color = '#000';
            this.style.color = '#000';
            filch("left");
        }
    };

    right.onmouseover = mouseOverFunction;
    right.onmouseout = mouseOutFunction;
    left.onmouseover = mouseOverFunction;
    left.onmouseout = mouseOutFunction;
