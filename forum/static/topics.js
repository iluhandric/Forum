var buts = document.getElementsByClassName('button');
     var pictures = document.getElementsByClassName('logot');
     var dict = {};
     var mouseOverFunction = function() {
          pictures[dict[this.id]].style.webkitFilter = "opacity(1)";
      };
       var mouseOutFunction = function() {
          pictures[dict[this.id]].style.webkitFilter = "opacity(0.8)";
      };
     for (var i = 0; i < buts.length; i++) {
         buts[i].onmouseover = mouseOverFunction;
         buts[i].onmouseout = mouseOutFunction;
         dict[buts[i].id] = i;
         pictures[dict[buts[i].id]].style.webkitFilter = "opacity(0.8)";
     }
