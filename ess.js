function id(elid){return document.getElementById(elid);}
window.onload = function (){
    var list = document.getElementsByTagName("style");
    for (i = 0; i < list.length; i++) {
        var l = list[i];
        /*console.log(l);*/
        if(l.type == "text/ess"){
            console.log('true');
            function ch(li, num){
	            try{
		            return li[num];
	            }
	            catch(err){
		            return "";
	            }
            }
            var tree = {};
            var vars = {};
            var comments = [];
            var p = l.innerHTML + "\n";
            /*console.log(p);*/
            var cur;
            var next;
            var word = "";
            var cname = "";
            var cproperty = "";
            var ident = false;
            var def = false;
            var comment = false;
            var un = true;
            var qmcom = false;
            var multiline = false;
            var usev = true;
            var start = true;
            for(i=0; i<p.length; i++){
	            last = ch(p, i - 1);
	            cur = p[i];
	            next = ch(p, i + 1);
	            if(cur == ":" && last != "\\" && comment == false){
		            tree[word] = {};
		            cname = word;
		            word = "";
		            usev = false;
		            start = false;
	            }
	            else if(cur == "/" && next == "*" && comment == false){
	                multiline = true;
	                un = false;
	                comment = true;
                }
                else if(cur == "*" && next == "/"){
                    multiline = false;
                    comment = false;
                    un = true;
                    comments.push(word);
                    word = "";
                }
                else if(cur == "?" && last != "\\" && comment == false && start == true){
                    comment = true;
                	qmcom = true;
                	un = true;
				}
				else if(cur == "#" && next == "!" && comment == false && start == true){
                    comment = true;
                	qmcom = true;
                	un = false;
				}
				else if(cur == "#" && next == "&" && comment == false && start == true){
                    comment = true;
                	qmcom = true;
                	un = false;
				}
	            else if(cur == "\t" && ident == false && comment == false){
		            ident = true;
	            }
	            else if(cur == "$" && last != "\\" && comment == false && usev == true){
		            def = true;
	            }
	            else if(cur == "=" && last != "\\" && comment == false){
		            cproperty = word;
		            word = "";
	            }
	            else if(cur == "\n" && last != ":" && comment == false){
		            /*console.log(word*/
		            if(word != ""){
			            if(def == false && cname != ""){
				            //cproperty[0] = "";
				            var text = word;
				            if(word.indexOf("$") > -1){
					            for(v in vars){
						            eval("text = text.replace(/\\" + v + "/g, '" + vars[v] + "');");
					            }
				            }
				            tree[cname][cproperty] = text;
			            }
			            else{
				            vars["$" + cproperty] = word;
			            }
		            }
		            word = "";
		            cproperty = "";
		            def = false;
		            start = true;
	            }
	            else if(cur == "\n" && qmcom == true && comment == true){
	                //console.log(word);
	            	comments.push(word);
	            	comment = false;
	            	qmcom = false;
                	word = "";
				}
	            else if(cur == "%" && comment == false && last != "\\" && start == true && def != true){
	            	word = word + "=";
				}
				else if(cur == "@" && last != "\\" && comment == false && start == true && def != true){
	            	word = word + "=";
				}
				else if(cur == "&" && comment == false && last != "\\" && def != true){
					word = word + ":";
				}
	            else if(cur == "\n" && next != "\t" && comment == false){
		            ident = false;
		            cname = "";
		            usev = true;
		            def = false;
	            }
	            else{
		            if(cur != "\t" && cur != "\n" && un == true && cur != "\\"){
			            word = word + cur;
		            }
		            if(cur == "\\" && next == "\\"){
		                word = word + cur;
                    }
		            un = true;
	            }
	            /*console.log(p[i]);
	            console.log(word);*/
                }
                function toCSS(tree){
	                var text = "";
	                for(t in tree){
		                text = text + "\n" + t + "{";
		                for(tt in tree[t]){
			                text = text + "\n\t" + tt + ":" + tree[t][tt] + ";";
		                }
		                text = text + "\n}\n"
	                }
	                return text;
                }
            /*console.log(tree);
            console.log(vars);
            console.log(comments);*/
            l.type = "text/css";
            l.innerHTML = toCSS(tree);
        }
        else{
            console.log('false');
        }
    }
};

