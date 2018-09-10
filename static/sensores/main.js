/**
 * Created by julian on 3/9/15.
 */
define(["dijit/form/FilteringSelect",
            "dijit/form/ComboBox",
            "dojo/data/ItemFileReadStore",
            "dojo/request/script",
            "dojo/deferred",
            "dojo/store/Memory",
            "dojo/parser",
            "dijit/form/DateTextBox",
            "dojo/date/locale",
            "dijit/layout/ContentPane",
            "dijit/layout/BorderContainer",
            "dijit/layout/TabContainer",
            "dojo/dom",
            "dojo/number",
            "dojox/widget/MonthAndYearlyCalendar",],
    function(){
       return function (empid,urlserver,token) {

        var selmes;
        var fecha;
        var colocadom = function (pondom, lugar) {
            require(["dojo/dom-construct"], function (domConstruct) {
                var node = domConstruct.toDom(pondom);
                domConstruct.place(node, lugar);
            });
        }

        var parambusca = '<table> <tr><td>Por Dia:</td></tr> ' +
                '<tr> <td> <div id="fechaSelect"></div></td> </tr> ' +
                '<tr><td>Por  Mes: </td> </tr> <tr> <td> <div id="mesSelect"></div> </td></tr>'+
                '<tr><td>Selección : </td> </tr> <tr> <td><div  id="filterSelect"></div> </td></tr>' +
                '<tr><td><div id="limpiaBoton"> </div> </td> </tr> </table>';

        var bc = dijit.layout.BorderContainer({
            liveSplitters: true, gutters: true,
        }, "appLayout");


        var header = new dijit.layout.ContentPane({
            region: 'top',
            splitter: true,
            content: '<h1><center>GRAFICAS SEGUIMIENTOS TEMPERATURAS</center> </h1>'
        });

        var cp1 = new dijit.layout.ContentPane({
            region: "left",
            splitter: true,
            style: "height: 100%; width: 15%;",
            content: parambusca
        });

        bc.addChild(header);


        var tc = new dijit.layout.TabContainer({ id: "Graficas", region: "center", style: "width: 100% ; height: 100% ", splitter: true, doLayout: false, });

        bc.addChild(tc);
        bc.addChild(cp1);


        // put the top level widget into the document, and then call startup()
        document.body.appendChild(bc.domNode);

        bc.startup();
        require(["dijit/registry", "dijit/form/Button"], function(registry,Button) {
            return new Button({
                label: "Limpiar",
                onClick: function () {
                    registry.byId("fechaSelect").set("value",null);
                    //registry.byId("mesSelect").set("value"," ");
                    registry.byId("mesSelect").onChange(null);
                    registry.byId("filterSelect").set("value",null);
                    fecha  = null;
                    selmes = null;

                }
            }, "limpiaBoton");
        });



        fecha = new dijit.form.DateTextBox(
                {
                    id: "fechaSelect",
                    name: "fechaSelect",
                    placeHolder: "Seleccione Fecha",
                    value: null,
                    onChange: function (fechaSelect) {

                        fecha = dojo.date.locale.format(fechaSelect, {datePattern: "ddMMyyyy", selector: "date"})

                    }
                }, "fechaSelect"
        );
        var selmes;

         fecha = new dijit.form.DateTextBox(
                {
                    id: "mesSelect",
                    name: "mesSelect",
                    placeHolder: "Seleccione Mes",
                    // constraints: {datePattern: 'MM/yyyy'},
                    popupClass:'dojox.widget.MonthAndYearlyCalendar',
                    onChange: function (fechaSelect) {
                        if (fechaSelect == null)
                        {
                            this._set("value",fechaSelect);
                            selmes= fechaSelect;
                        }else
                        {
                            selmes = dojo.date.locale.format(fechaSelect, {datePattern: "MMyyyy", selector: "date"})
                        }

                    }


                }, "mesSelect"
        );




        var d = new dojo.Deferred;


        d.addCallbacks(function (dataequipo) {
            var equiposData = new dojo.store.Memory({data: dataequipo});


            var select = new dijit.form.ComboBox({
                id: "filterSelect",
                name: "equipos",
                style: "width: 100%;",
                placeHolder: "Selecione Equipo",
                store: equiposData,
                searchAttr: "equipos",
                onChange: function (filterSelect) {
                    //console.log("combobox onchange ", filterSelect, this.item);
                    idsonda = dijit.byId('filterSelect').item.tracksondas
                    var urlbusca = urlserver+"rest_loaddata/sensorfecha/"


                    if (typeof fecha == 'string'){
                        var tipo= "HH:mm"
                        var tabtil = fecha;
                        var xhrArgs1 = {
                            url: urlbusca,
                            content: {
                                empid: empid,
                                fecha: fecha,
                                idsonda: idsonda
                            },
                            headers: {'Authorization': token },
                            handleAs: "json",

                        }
                    }
                    if ( typeof selmes == 'string'){
                        var tipo="dd HH:mm"
                        var tabtil= selmes;
                        var xhrArgs1 = {
                            url: urlbusca,
                            content: {
                                empid: empid,
                                selmes: selmes,
                                idsonda: idsonda
                            },
                            headers: {'Authorization': token },
                            handleAs: "json",

                        }
                    }



                    if (typeof fecha == 'string'  || typeof selmes == 'string') {

                        var titulografica = filterSelect;

                        var domgrafica = idsonda + tabtil;

                        var idegrafica = '<div id="' + domgrafica + '"style="height: 650px; width: 100%;"></div>';
                        tab = new dijit.layout.ContentPane({ id: "tab" + domgrafica, title: tabtil, style: "height: 100%; width: 100%;", closable: true });

                        tc.addChild(tab);
                        tc.selectChild(tab);


                        colocadom(idegrafica, "tab" + domgrafica)


                        require(["sensores/grafica"], function(grafica){
                            return new grafica(xhrArgs1, domgrafica, titulografica,tipo);
                        });


                        delete tab;
                    }
                    else
                    {
                        require(["dijit/ConfirmDialog", "dojo/domReady!"], function(ConfirmDialog){
                        dialogo = new ConfirmDialog({
                            title: "Atención",
                            content: "Debe seleccionar una fecha",
                            style: "width: 300px"
                        });
                        dialogo.show();
                    }
                        )};
                }
            }, "filterSelect");

            select.startup();


        })

    var utlsensor  =  urlserver+"rest_appcc/detregsensor/" ;
    var xhrArgs = {
            url: utlsensor,
            content: {
                empid: empid
            },
            headers: {'Authorization': token },
            handleAs: "json",
            load: function (response) {
                //console.log(response)
                d.callback(response);
            }
        }

        var cargaDetReg = dojo.xhrGet(xhrArgs);
    }

    });
