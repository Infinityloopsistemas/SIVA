/**
 * Created by julian on 3/9/15.
 */
define(["dijit/registry","dojox/charting/Chart", "dojox/charting/themes/PlotKit/blue", "dojo/number", "dojo/store/Observable", "dojo/store/Memory", "dojo/json", "dojo/request/script", "dojo/query", "dojo/dom-construct", "dojo/json", "dojo/on", "dojox/charting/StoreSeries", "dojox/charting/plot2d/Default", "dojox/charting/plot2d/Grid", "dojox/charting/plot2d/Lines", "dojox/charting/axis2d/Default", "dojox/charting/action2d/Tooltip", "dojo/domReady!"],
            function (registry,Chart, Harmony, number, Observable, Memory, StoreSeries, script, Tooltip) {
                return function (xhrArgs1, domgrafica, titulografica,tipo) {

                registry.byId("tab" + domgrafica).resize();

                var output =[];
                var outputx =[];
                var outputy =[];
                var xhrLoaded = function (results) {

                    for (var i = 0; i < results.length; i++) {
                        var detail = results[i];
                        //output.push({ Temp: detail.Temperature , Fecha : detail.date, Serie: 1 })
                        outputx.push(detail.date)
                        outputy.push(Number(detail.Temperature))
                        output.push({"x": detail.date, "y": Number(detail.Temperature), "sensor": detail.tracksonda})
                    }

                    //console.log(output);
                    store = Observable(new Memory({
                        data: output

                    }));


                    chart = new Chart(domgrafica, {
                        title: titulografica,
                        titlePos: "top",
                        titleGap: 25,
                        titleFont: "normal normal normal 20pt Arial",
                        titleFontColor: "blue"
                    });

                    // Set the theme
                    chart.setTheme(dojox.charting.themes.PlotKit.blue);


                    // Add the only/default plot
                    chart.addPlot("Grid", {
                        type: "Grid",
                        markers: true,
                        hMajorLines: true,
                        hMinorLines: true,
                        vMajorLines: true,
                        vMinorLines: true,
                        tension: 3


                    });

                    var minX = Math.min.apply(Math, output.map(function (val) {
                        return val.x;
                    }));
                    var maxX = Math.max.apply(Math, output.map(function (val) {
                        return val.x;
                    }));

                    // Add axes
                    chart.addAxis("x", {
                        fixLower: minX,
                        fixUpper: maxX,
                        minorTicks: true,
                        natural: true, stroke: "grey",
                        majorTick: {stroke: "black", length: 4},
                        minorTick: {stroke: "gray", length: 2},
                        labelFunc: function (n) {
                            //console.log(n);
                            var date = new Date(dojo.number.parse(n));
                            //console.log(date);
                            return dojo.date.locale.format(date, {
                                    selector: "date",
                                    datePattern: tipo });
                                    }
                        });

                    var minY = Math.min.apply(Math, output.map(function (val) {
                        return val.y;
                    }));
                    var maxY = Math.max.apply(Math, output.map(function (val) {
                        return val.y;
                    }));

                    chart.addAxis("y", {vertical: true, fixLower: minY, fixUpper: maxY, minorTickStep: 1});

                    // Add the storeseries - Query for all data

                    //var serie = new dojox.charting.StoreSeries({ query: { tracksonda: 1}}, "date")
                    chart.addSeries("Sonda 1", output);
                    //chart.addSeries("Sonda 1", new dojox.charting.StoreSeries(store, {query: {sensor: 1}}, "y"));
                    //chart.addSeries("Sonda 2", new dojox.charting.StoreSeries( store, {query: { sensor: 7} }, "y"));
                    //chart.addSeries("Sonda 3", new dojox.charting.StoreSeries( store, {query: { sensor: 8} }, "y"));
                    // Render the ch

                    var tip = new Tooltip(this.chart, "default", { 'class': 'kaboom' });

                    chart.render();


                }

                //var jsonvar = JSON.stringify(data);
                var cargaCurvas = dojo.xhrGet(xhrArgs1).then(function(data){ xhrLoaded(data) } );


            };

})