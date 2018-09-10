/**
 * Created by julian on 3/9/15.
 */
define(["dojo/_base/declare"], function(declare) {
    declare("sensores.globales", null, {
        store: null,
        outputx: null,
        outputy: null,
        output: null,
        grafica: null,
        colocadom: null,
        fecha: null,
        selmes: null,

        constructor: function () {
            this.store = "";
            this.outputx = [];
            this.outputy = [];
            this.output = [];
            this.grafica = "";
            this.colocadom = "";
            this.fecha = "";
            this.selmes = "";


        }

    })
});