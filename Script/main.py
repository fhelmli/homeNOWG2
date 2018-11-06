#!/usr/bin/env python2

import imp
try:
    imp.find_module('ui')
    found = True
except ImportError:
    found = False

################################
inAnApp = False
if found:
    inAnApp = True
################################

if inAnApp:
	import ui
import os
import threading
import socket
import SimpleHTTPServer
import BaseHTTPServer
import time

from hmscripts import testHMScripts


#######################################################
# our new bundle ID for iOS App: at.homenow.homenow2
#######################################################


numTetrisGames = 1


hostName = ""
hostPort = 8083

# TEST! show all results of all "get all infos" HMScripts
allCCUInfoInOne = testHMScripts()


BaseHTTPRequestHandler = SimpleHTTPServer.SimpleHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):

	#	GET is for view getting data from view controller (= a HTTP server in our case)
	def do_GET(self):
		self.send_response(200, 'OK')
		self.send_header('Content-type', 'html')
		self.end_headers()
		
		if self.path=='/oachkatzlschwoaf0815':
			pass
		else:
			myServer.server_close()
			return
		self.wfile.write(bytes("<html><body>" + allCCUInfoInOne))
		for x in range(numTetrisGames):
			self.wfile.write(bytes(
				"""
				<h1><p>NEW TEST FOR CONTINUOUS INTEGRATION!</p>This WebView content was written in Python! Additional data sent from Python code: """
					 + str(x) + """<p><p>Tetris game in SVG:</h1>
			
				<svg width="220px" height="120px">
     <text font-size="32"  x="25" y="60" fill="green">
            Hello, World!
    </text>
</svg>
				
				<span width="500px" height="1200px">
				<svg width="100%" height="100%">
				<!--
				<text x="1" y="1" font-size="32px">Mozilla SVG Tetris - Press 'h' for help.</text>-->
				
				<g transform="scale(40 40)">
				
				<g id="preview"""+str(x)+"""" stroke-width="0.02"/>
				<g id="board"""+str(x)+"""" stroke-width="0.02"/>
				
				</g>
				
				</svg>
				
				</span>
				
				<script>
				
				//document.body.innerHTML += 'cool';
				
				
				
			//	try {
					
					
				
				//----------------------------------------------------------------------
				// static data
				
				var SVG_NS ="http://www.w3.org/2000/svg";
				var tickTimeReducer = 0.98;
				var ROWS = 20;
				var COLS = 10;
				
				var HPAD = 2; // horizontal padding used in laying out grids
				var VPAD = 2; // ditto for vertical
				
				var SHAPE_DESCRIPTORS = [
				  { color: "grey",   orientations: [ [[0,0],[1,0],[0,1],[1,1]] ] },
				  { color: "blue",   orientations: [ [[0,0],[1,0],[2,0],[2,1]],
				                                     [[1,0],[1,1],[1,2],[0,2]],
				                                     [[0,0],[0,1],[1,1],[2,1]],
				                                     [[0,0],[1,0],[0,1],[0,2]] ] },
				  { color: "purple", orientations: [ [[0,0],[0,1],[1,0],[2,0]],
				                                     [[0,0],[1,0],[1,1],[1,2]],
				                                     [[0,1],[1,1],[2,1],[2,0]],
				                                     [[0,0],[0,1],[0,2],[1,2]] ] },
				  { color: "cyan",   orientations: [ [[0,0],[1,0],[2,0],[3,0]],
				                                     [[0,0],[0,1],[0,2],[0,3]] ] },
				  { color: "green",  orientations: [ [[1,0],[2,0],[0,1],[1,1]],
				                                     [[0,0],[0,1],[1,1],[1,2]] ] },
				  { color: "red",    orientations: [ [[1,0],[1,1],[0,1],[0,2]],
				                                     [[0,0],[1,0],[1,1],[2,1]] ] },
				  { color: "yellow", orientations: [ [[0,1],[1,1],[2,1],[1,0]],
				                                     [[0,0],[0,1],[0,2],[1,1]],
				                                     [[0,0],[1,0],[2,0],[1,1]],
				                                     [[1,0],[1,1],[1,2],[0,1]] ] }
				];
				
				
				
				//----------------------------------------------------------------------
				// Helper functions
				
				// map a function over an array; accumulate output in new array:
				function mapcar(f, a) {
				  var res = new Array(a.length);
				  for (var i=0;i<a.length;++i) {
				    res[i] = f(a[i]);
				  }
				  return res;
				}
				
				// map a function over an array; don't accumulate output:
				function mapc(f, a) {
				  for (var i=0;i<a.length;++i) {
				    f(a[i]);
				  }
				}
				
				// return true if predicate p is true for every element of the array:
				function every(p, a) {
				  for (var i=0;i<a.length;++i) {
				    if (!p(a[i])) return false;
				  }
				  return true;
				}
				
				function suspendRedraw()
				{
				  // asv doesn't implement suspendRedraw, so we wrap this in a try-block:
				  try {
				    document.documentElement.suspendRedraw(0);
				  }
				  catch(e) {}
				}
				
				function unsuspendRedraw()
				{
				  // asv doesn't implement unsuspendRedraw, so we wrap this in a try-block:
				  try {
				    document.documentElement.unsuspendRedraw(0);
				  }
				  catch(e) {}
				}
				
				
				
				//----------------------------------------------------------------------
				// Shape class
				
				function Shape(position) {
				  // create a new shape, randomly picking a descriptor & orientation:
				  this._descriptor = SHAPE_DESCRIPTORS[Math.round(Math.random()*(SHAPE_DESCRIPTORS.length-1))];
				  this._orientation = Math.round(Math.random()*(this._descriptor.orientations.length-1));
				  this._pos = position;
				}
				
				Shape.prototype = {
				  getCellArray : function() {
				    var s = this;
				    return mapcar(function(coord) { return [coord[0]+s._pos[0],coord[1]+s._pos[1]]; },
				               this._descriptor.orientations[this._orientation]);
				  },
				  getColor : function() {
				    return this._descriptor.color;
				  },
				  move : function(dx,dy) {
				    this._pos[0] += dx; this._pos[1] += dy;
				  },
				  rotate : function(dOrient) {
				    this._orientation = (this._orientation+dOrient) % this._descriptor.orientations.length;
				    if (this._orientation<0) this._orientation += this._descriptor.orientations.length;
				  }
				};
				
				//----------------------------------------------------------------------
				// Grid class
				
				function Grid(cols, rows, color, bordercolor, x, y, width, height, node) {
				  // Create a cols*rows grid with a 1/2-cell border.
				  // Scale to fit width*height user pixels (including border).
				  // Place at x,y user pixel coords.
				
				  this._cols = cols;
				  this._rows = rows;
				  this._color = color;
				
				  node.setAttribute("transform", "translate("+x+","+y+") scale("+
				                                 (width/(cols+1))+","+(height/(rows+1))+") translate(0.5,0.5)");
				
				  this._border = document.createElementNS(SVG_NS, "rect");
				  this._border.setAttribute("fill", bordercolor);
				  this._border.setAttribute("width", cols+1);
				  this._border.setAttribute("height", rows+1);
				  this._border.setAttribute("x", "-0.5");
				  this._border.setAttribute("y", "-0.5");
				
				  this._background = document.createElementNS(SVG_NS, "rect");
				  this._background.setAttribute("fill", color);
				  this._background.setAttribute("width", cols);
				  this._background.setAttribute("height", rows);
				
				  this._rowArray = document.createElementNS(SVG_NS, "g");
				  for (var r=0;r<rows;++r) {
				    var row_group = document.createElementNS(SVG_NS, "g");
				    row_group.setAttribute("transform", "translate(0,"+r+")");
				
				    for (var c=0;c<cols;++c) {
				      var cell = document.createElementNS(SVG_NS, "rect");
				      cell.setAttribute("x", c);
				      cell.setAttribute("width", "1");
				      cell.setAttribute("height", "1");
				      cell.setAttribute("stroke", "grey");
				      cell.setAttribute("fill", "none");
				      cell.occupied = false;
				      row_group.appendChild(cell);
				    }
				    this._rowArray.appendChild(row_group);
				  }
				  
				  node.appendChild(this._border);
				  node.appendChild(this._background);
				  node.appendChild(this._rowArray);
				}
				
				Grid.prototype = {
				  colorCell : function(coord, color) { try {
				    this._rowArray.childNodes.item(coord[1]).childNodes.item(coord[0]).setAttribute("fill", color);  
				}catch(e) {
				alert("error: coord="+coord);
				}
				  },
				  clearCell : function(coord) {
				    this.colorCell(coord, this._color);
				  },
				  occupyCell : function(coord) {
				// XXX ASV has a problem with expando properties, so we use attribs instead:
				//    this._rowArray.childNodes.item(coord[1]).childNodes.item(coord[0]).occupied = true;
				    this._rowArray.childNodes.item(coord[1]).childNodes.item(coord[0]).setAttribute("occupied", "true");
				  },
				  unoccupyCell : function(coord) {
				//    this._rowArray.childNodes.item(coord[1]).childNodes.item(coord[0]).occupied = false;
				    this._rowArray.childNodes.item(coord[1]).childNodes.item(coord[0]).setAttribute("occupied", "false");
				  },
				  cellInBounds : function(coord) {
				    return (coord[0]>=0 && coord[1]>=0 && coord[0]<this._cols && coord[1]<this._rows);
				  },
				  cellOccupied : function(coord) {
				//    return this._rowArray.childNodes.item(coord[1]).childNodes.item(coord[0]).occupied;
				    return this._rowArray.childNodes.item(coord[1]).childNodes.item(coord[0]).getAttribute("occupied")=="true";
				  },
				  eliminateFullRows : function() {
				    var g = this;
				    var bo = false;
				    function rowFull(r) {
				      for (var c=0;c<g._cols;++c) {
				        if (!g.cellOccupied([c,r])) return false;
				      }
				      return true;
				    }
				
				    function moveCellDown(c,r) {
				      var src = g._rowArray.childNodes.item(r).childNodes.item(c);
				      var dest = g._rowArray.childNodes.item(r+1).childNodes.item(c);
				      dest.setAttribute("fill", src.getAttribute("fill"));
				      //dest.occupied = src.occupied;
				      //src.occupied = false;
				      dest.setAttribute("occupied", src.getAttribute("occupied"));
				      src.setAttribute("occupied", "false");
				      src.setAttribute("fill", g._color);
				    }
				    
				    function eliminateRow(row) {
				      suspendRedraw();
				      for (var c=0;c<g._cols;++c) {
				        g.clearCell([c,row]);
				        g.unoccupyCell([c,row]);
				      }
				      for (var r=row-1;r>=0;--r) {
				        for (c=0;c<g._cols;++c) {
				          if (g.cellOccupied([c,r])) 
				            moveCellDown(c,r);
				        }
				      }
				      unsuspendRedraw();
				    }
				
				    for (var r=0;r<this._rows;++r) {
				      if (rowFull(r)) {
				        bo = true;  
				        eliminateRow(r);
				        ++lines;
				      }
				    }
				    if (bo) {
				      tickTime=time(tickTime);
				    }
				  }
				};
				
				//----------------------------------------------------------------------
				// message class
				
				function Message(txt, position, style) {
				  this._node = document.createElementNS(SVG_NS, "text");
				  this._node.setAttribute("style", style);
				  this._node.setAttribute("x", position[0]);
				  this._node.setAttribute("y", position[1]);
				  this._node.appendChild(document.createTextNode(txt));
				}
				
				Message.prototype = {
				  show : function() {
				    suspendRedraw();
				    document.documentElement.appendChild(this._node);
				    unsuspendRedraw();
				  },
				  hide : function() {
				    document.documentElement.removeChild(this._node);
				  }
				};
				
				
				
				
				
				//----------------------------------------------------------------------
				// grid shape operations
				
				function canPlace(shape, grid) {
				  // can only place if all cells in shape are in bounds and not occupied:
				  return every(function(coord){ return grid.cellInBounds(coord) &&
				                                       !grid.cellOccupied(coord); },
				                shape.getCellArray());
				}
				
				function show(shape, grid) {
				  suspendRedraw();
				  mapc(function(coord){ grid.colorCell(coord, shape.getColor()); },
				       shape.getCellArray());
				  unsuspendRedraw();
				}
				
				function hide(shape, grid) {
				  suspendRedraw();
				  mapc(function(coord){ grid.clearCell(coord); },
				       shape.getCellArray());
				  unsuspendRedraw();
				}
				
				function occupy(shape, grid) {
				  mapc(function(coord){ grid.occupyCell(coord); },
				       shape.getCellArray());
				}
				
				function move(shape, grid, dx, dy) {
				  shape.move(dx,dy);
				  if (!canPlace(shape, grid)) {
				    shape.move(-dx,-dy);
				    return false;
				  }
				  suspendRedraw();
				  shape.move(-dx, -dy);
				  hide(shape, grid);
				  shape.move(dx,dy);
				  show(shape, grid);
				  unsuspendRedraw();
				  return true;
				}
				
				function rotate(shape, grid, dOrient) {
				  shape.rotate(dOrient);
				  if (!canPlace(shape, grid)) {
				    shape.rotate(-dOrient);
				    return false;
				  }
				  suspendRedraw();
				  shape.rotate(-dOrient);
				  hide(shape, grid);
				  shape.rotate(dOrient);
				  show(shape, grid);
				  unsuspendRedraw();
				  return true;
				}
				
				function drop(shape, grid) {
				  suspendRedraw();
				  while (move(shape, grid, 0, 1))
				    /**/;
				  unsuspendRedraw();
				}
				
				//----------------------------------------------------------------------
				// the game:
				
				var board;   // grid where the action is
				var preview; // grid where the next shape will be previewed
				var currentShape; 
				var lines;
				var score;
				var nextShape; 
				var gameState; // "stopped", "running", "finished"
				var tickTime;
				function startNewGame() {
				  // XXX clear grids
				  score = 0;
				  suspendRedraw();
				  currentShape = new Shape([3,0]);
				  lines = 0;
				  show(currentShape, board);
				  nextShape = new Shape([0,0]);
				  show(nextShape, preview);
				  unsuspendRedraw();
				  gameState = "running";
				  tickTime = 300;
				  tick();
				  
				  
				  
				  setTimeout(function()  
				  	{ 
				  		
				  		/*board = new Grid(COLS, ROWS, "black", "grey", HPAD, VPAD, COLS+1, ROWS+1, document.getElementById("board""" + str(x)+""""));
				  
				  preview = new Grid(4,4, "black", "grey", 2*HPAD+COLS+1, VPAD, 5, 5, document.getElementById("preview""" +str(x)+""""));*/
				  		
				  		gameState="running"; 
				  		//startNewGame(); 
				  		
				  		//location.reload();
				  		},
				  3000);
			  }
				
				function runNextShape() {
				  occupy(currentShape, board);
				  board.eliminateFullRows();
				  score = score+1;
				  suspendRedraw();
				  currentShape = nextShape;
				  hide(nextShape, preview);
				  currentShape.move(3,0);
				  if (!canPlace(currentShape, board)) {
				    unsuspendRedraw();
				    return false; // game over!
				  }
				  show(currentShape, board);
				  nextShape = new Shape([0,0]);
				  show(nextShape, preview);
				  unsuspendRedraw();
				  return true;
				}
				
				function tick() {
				  if (gameState != "running") return;
				
				  if (!move(currentShape, board, 0, 1)) {
				    if(!runNextShape()) {
				      var m = new Message("Game Over! Score:"+score, [1,10], "stroke:none;font-size:2px;fill:red;stroke:black;stroke-width:0.04px;fill-opacity:0.8;");
				      m.show();
				      gameState = "finished";
				      return; // Game over
				    }
				  }
				  setTimeout("tick()", tickTime);
				}
				
				function time(tickTime) {
				  tickTime = tickTime*tickTimeReducer;
				  return tickTime;
				}
				
				function pause() {
				  if (gameState == "running")
				    gameState = "stopped";
				}
				
				function resume() {
				  if (gameState == "stopped") {
				    gameState = "running";
				    tick();
				  }
				}
				
				
				
				
				
				//----------------------------------------------------------------------
				// user input handler
				
				/*function keyHandler(event) {
				  event.preventDefault();
				  switch (event.keyCode) {
				    case 32:
				      if (gameState == "running")
				        drop(currentShape, board);
				      break;
				    case 72:
				      pause();
				      alert("Help:\n"+
				            "-------------------------------------\n\n"+
				            "Score : "+score+"\n"+
				            "Lines : "+lines+"\n"+
				            "h : Display this help\n"+
				            "p : Toggle pause game\n"+
				            "up    : Rotate piece counterclockwise\n"+
				            "down  : Rotate piece clocwise\n"+
				            "left  : Move piece left\n"+
				            "right : Move piece right\n"+
				            "space : Drop piece\n");
				      resume();
				      break;
				    case 80:
				      if (gameState == "running") 
				        pause();
				      else
				        resume();
				      break;
				    case 38:
				      if (gameState == "running")
				        rotate(currentShape, board, -1);
				      break;
				    case 40:
				      if (gameState == "running")
				        rotate(currentShape, board, 1);
				      break;
				    case 37:
				      if (gameState == "running")
				        move(currentShape, board, -1, 0);
				      break;
				    case 39:
				      if (gameState == "running")
				        move(currentShape, board, 1, 0);
				      break;
				  }
				}
				
				//----------------------------------------------------------------------
				
				*/
				
				//document.body.innerHTML += "END";		
				
				
				document.documentElement.
					setAttribute("viewBox", "0 0 100 100"); //+(1*(3*HPAD+(COLS+1)+5))+" "+
					//(1*(2*VPAD+(ROWS+1)));
			
				  board = new Grid(COLS, ROWS, "black", "grey", HPAD, VPAD, COLS+1, ROWS+1, document.getElementById("board""" + str(x)+""""));
				  
				  preview = new Grid(4,4, "black", "grey", 2*HPAD+COLS+1, VPAD, 5, 5, document.getElementById("preview""" +str(x)+""""));
				
				  startNewGame();
				  
				  
				
				
				
	
				  // initialize event processing:
				  //document.documentElement.
				  addEventListener("keydown", keyHandler, false);
				
				
				
		
				document.body.innerHTML += "END";		
				
				
				//} catch (e) {
			//		document.body.innerHTML += e.message;
			//	}
				
				</script>

				
				
				
				""")) # % str(x))) # self.path, "utf-8"))
		
		self.wfile.write(bytes("""
		
			<h1>Interactive 3D Transforms Test:</h1>
			
			
			<style type="text/css" media="screen">
				
				/* Add style rules here */
				* { box-sizing: border-box; }

body { font-family: sans-serif; }

.scene {
  width: 200px;
  height: 200px;
  border: 1px solid #CCC;
  margin: 80px;
  perspective: 400px;
}

.cube {
  width: 200px;
  height: 200px;
  position: relative;
  transform-style: preserve-3d;
  transform: translateZ(-100px);
  transition: transform 1s;
}

.cube.show-front  { transform: translateZ(-100px) rotateY(   0deg); }
.cube.show-right  { transform: translateZ(-100px) rotateY( -90deg); }
.cube.show-back   { transform: translateZ(-100px) rotateY(-180deg); }
.cube.show-left   { transform: translateZ(-100px) rotateY(  90deg); }
.cube.show-top    { transform: translateZ(-100px) rotateX( -90deg); }
.cube.show-bottom { transform: translateZ(-100px) rotateX(  90deg); }

.cube__face {
  position: absolute;
  width: 200px;
  height: 200px;
  border: 2px solid black;
  line-height: 200px;
  font-size: 40px;
  font-weight: bold;
  color: white;
  text-align: center;
}

.cube__face--front  { background: hsla(  0, 100%, 50%, 0.7); }
.cube__face--right  { background: hsla( 60, 100%, 50%, 0.7); }
.cube__face--back   { background: hsla(120, 100%, 50%, 0.7); }
.cube__face--left   { background: hsla(180, 100%, 50%, 0.7); }
.cube__face--top    { background: hsla(240, 100%, 50%, 0.7); }
.cube__face--bottom { background: hsla(300, 100%, 50%, 0.7); }

.cube__face--front  { transform: rotateY(  0deg) translateZ(100px); }
.cube__face--right  { transform: rotateY( 90deg) translateZ(100px); }
.cube__face--back   { transform: rotateY(180deg) translateZ(100px); }
.cube__face--left   { transform: rotateY(-90deg) translateZ(100px); }
.cube__face--top    { transform: rotateX( 90deg) translateZ(100px); }
.cube__face--bottom { transform: rotateX(-90deg) translateZ(100px); }

label { margin-right: 10px; }
				
			</style>
		
		
		"""))
		
		for i in range(3):
			self.wfile.write(bytes("""

			<div class="scene">
  <div class="cube">
    <div class="cube__face cube__face--front">front</div>
    <div class="cube__face cube__face--back">back</div>
    <div class="cube__face cube__face--right">right</div>
    <div class="cube__face cube__face--left">left</div>
    <div class="cube__face cube__face--top">top</div>
    <div class="cube__face cube__face--bottom">bottom</div>
  </div>
</div>
			"""))



		self.wfile.write(bytes("""



<p class="radio-group">
  <label>
    <input type="radio" name="rotate-cube-side" value="front" checked /> front
  </label>
  <label>
    <input type="radio" name="rotate-cube-side" value="right" /> right
  </label>
  <label>
    <input type="radio" name="rotate-cube-side" value="back" /> back
  </label>
  <label>
    <input type="radio" name="rotate-cube-side" value="left" /> left
  </label>
  <label>
    <input type="radio" name="rotate-cube-side" value="top" /> top
  </label>
  <label>
    <input type="radio" name="rotate-cube-side" value="bottom" /> bottom
  </label>
</p>
		"""))
			
			
		self.wfile.write(bytes("""

			<script>
			
			
			var cube = document.querySelectorAll('.cube');
var radioGroup = document.querySelector('.radio-group');
var currentClass = '';

function changeSide() {
  var checkedRadio = radioGroup.querySelector(':checked');
  var showClass = 'show-' + checkedRadio.value;
  if ( currentClass ) {
    cube[0].classList.remove( currentClass );
    cube[1].classList.remove( currentClass );
    cube[2].classList.remove( currentClass );
  }
  cube[0].classList.add( showClass );
  cube[1].classList.add( showClass );
  cube[2].classList.add( showClass );
  currentClass = showClass;
}
// set initial side
changeSide();

radioGroup.addEventListener( 'change', changeSide );		
			
			
			</script>
			
			"""))
			
		
		for i in range(1000):
			self.wfile.write(bytes("""
				<h1>All content was sent to the WebView from Python code. Additional data: %s<p><p>Simple SVG file:</h1>
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 68 65">
				<path fill="#1A374D" d="M42 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v21l12 15-7 15.7c14.5 13.9 35 2.8 35-13.7 0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
				<path d="M14 27v-20c0-3.7-3.3-7-7-7s-7 3.3-7 7v41c0 8.2 9.2 17 20 17s20-9.2 20-20c0-13.3-13.4-21.8-26-18zm6 25c-3.9 0-7-3.1-7-7s3.1-7 7-7 7 3.1 7 7-3.1 7-7 7z"/>
				</svg>
				
				
			""" % str(i))) # self.path, "utf-8"))
		
		#time.sleep(2.0)
		
		if inAnApp:
			myServer.server_close()

		
	def log_message(self, format, *args):
		pass


myServer = BaseHTTPServer.HTTPServer((hostName, hostPort), MyServer)

#print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))


def worker(q):
	try:
		myServer.serve_forever()
	#except KeyboardInterrupt:
	#	pass
	except:
		pass
	
	myServer.server_close()
	#print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))
	
	
	




if inAnApp:
	t = threading.Thread(target=worker, args=(0,))
	t.daemon = True
	t.start()
	
	#time.sleep(1.0)
	
	file_path = os.path.abspath('html/main.html')
	
	v = ui.load_view()
	
	v['webview1'].load_url('http://localhost:' + str(hostPort) + '/oachkatzlschwoaf0815')
	
	#v['webview1'].load_url(file_path)
	
	v.present(style='sheet', title_bar_color='#000000',
	#hide_close_button=True,
	hide_title_bar=True,
	animated=False)
	#orientations=['portrait'])

else:
	worker(0)


# HTML zu Python: (User-Events, Seite geladen): Ajax zum HTTP-Server

# Python zu HTML: Ajax in Dauerschleife, wenn Jacascript-Antwort von Python kommt: dieses ausfuehren

# events von SVGs und buttons etc. zu Python, und z.B. redrawWidget, redrawWindow, redrawPage-events ueber Ajax u Python

#Editier-stuff: native UI-Elemente mit der Portablen LIb fuer Kivy und Pythonista ueber dem WebView einblenden

#Translation-File in Python, das alles auch im HTML und SVG uebersetzt, HTML und SVG muessen Englisch sein
