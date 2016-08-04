$('.left_Navigator #controls .second_level li a').click(function(){
    if($(this).parent().hasClass("selected")){
        $(this).parent().removeClass("selected");
    }
    else{
        $(this).parent().addClass("selected");
        var pdata = d3.json("/getDataCSV",function(error,data){
        RenderData(data);
        console.log("Hello");   
        } 
});


})

$('.left_Navigator ul  #status_control').focus(function(){
    
    $(this).css("background-color","yellow");

})


//Set up properies 
var height = 500;
var width=960;
var margin=15;
var radius  = Math.min(width, height) / 2;
//Color scale generator
var color = d3.scaleOrdinal().range(d3.schemeCategory10);
//Generate arc with given arguments
var arc = d3.arc()
            .outerRadius(radius)
            .innerRadius(40)
            .padAngle(0.1); 

//Constructs a new pie generator with the default settings.
var labelArc = d3.arc()
                 .outerRadius(radius - 15)
                 .innerRadius(radius-55);

//Constructs a new pie generator with the default settings.
var pie = d3.pie()
          .sort(null)
          .value(function(d) {  
                              console.log(d['Duration']);
                              return d['Duration']; });


var svg = d3.select("body .monitor #main #in_the_middle")
            .append("svg")
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");



function RenderData(da){
     console.log(da);
    
    var g = svg.selectAll(".arc")
               .data(pie(da))
               .enter()
               .append("g")
               .attr("class", "arc");

    g.append("path")
      .attr("d", arc)
      .style("fill", function(d) { return color(d['data']['Duration']); });

    g.append("text")
      .attr("transform", function(d) { return "translate(" + labelArc.centroid(d) + ")"; })
      .attr("dy", ".35em")
      .text(function(d) { console.log(d['data']['Name']);
                          return d['data']['Name']; })  
    
}
