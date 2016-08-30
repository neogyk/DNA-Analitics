var twoCdata ;
var Special=[];
function item(name,value){
         this.name = name;
         this.value = value;
}
$(document).ready(function(){
        $.getJSON($SCRIPT_ROOT+'/getDataCSV',{},function(dataJson){
                console.log(dataJson);
                for (i in dataJson.name){
                  var a  =  new item (dataJson.name[i],dataJson.value[i]);
                  console.log(a);
                  Special.push(a);
                }
          });
         return false;
});
      
$("[class$=-inverse]").click(function(){
        console.log(Special);
        //Enter
        d3.select("div#main").selectAll('div').data(Special).enter().append('div').attr('class', 'item')
            .append('div').attr('class', 'data').append('span');
        //Update
        d3.select("#main").selectAll('div.item').data(Special)
            .select('div').style('width', function (d) { return (d.value*2) + 'px';})
            .select('span').text(function (d) { return d.value;});
        d3.select("#main").selectAll('div.item').data(Special).append('div').attr('class', 'name')
            .text(function (d) {return d.name;});
        // Exit
        d3.select("#main").selectAll('div.item').data(Special).exit().remove();
});
   

var data = [{name: "Layout", value: 286},
            {name: "Animation", value: 92},
            {name: "FTP", value: 74},
            {name: "Paint", value: 56},
            {name: "Lookdev", value: 40},
            {name: "Compositing", value: 32},
            {name: "Baking", value: 29},
            {name: "Rendering", value: 24},
            {name: "Cloth", value: 23},
            {name: "Hair and Fur", value: 16},
            {name: "Assemble", value: 11},
            {name: "hair and fur", value: 7},
            {name: "fx", value: 7},
            {name: "Fur", value: 3},
            {name: "Modeling", value: 1}]
var width = 960;
var height = 500;
var event = [];
var barchart=d3.select('.barchart')
              .attr('width',width+100)
              .attr('height',height);
var barWidth = width / data.length;
var bar  = barchart.selectAll("g").data(data).enter().append("g")
        .attr("transform", function(d, i) { return "translate(" + i * barWidth + ",0)"; })
        .text(function(d){return d.name;});
    bar.append('rect').attr("y", function(d) { return d.value })
                    .attr("height", function(d) { return height - d.value })
                    .attr("width", barWidth - 1)
                    .attr('style','fill:rgb(81,135,161);');
    bar.append('text').attr('transform','rotate(-90)')
                    .attr('class','description')
                    .attr("x", function(d) { return -(height)/1.25; })//-(height)/1.25
                    .attr("y", barWidth/2)
                    .text(function(d){return d.name;});
    bar.append('rect').attr('class','description-form')
                    .attr('width',barWidth-1)
                    .attr('height',50)
                    .attr("y", function(d) { return d.value-5; });
    bar.append('text').attr("y", function(d) { return d.value-5; })
                  .attr('width',barWidth-1)
                  .attr('height',50)
                  .attr("x", function(d) { return height - d.value ; })
                  .text(function(d){return d.value;});      

      

$('#get_twoColumnData').click(function(){
         
          $.getJSON($SCRIPT_ROOT+"/twoColumnDataCSV",{},function(outData){  
            console.log(outData);
            twoCdata = outData;
          });
          return false;
});
      
      //Data loaded 
   //TO DO
   /*
   1) make list of object -['name':,'status'] -- Done
   There are another way to Produce Functionality of code:
   
   2) make diagram -- Done
      
   3) make bar chart
   
   4) make pie chart
   
   4) make 3d bar graph
   
   5) provide tim flow
   
   6) make Controls
   
   7) admin Page    
   */
      