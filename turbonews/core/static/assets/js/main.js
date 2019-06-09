$(document).ready(function(){

	$("#updateButton").on("click", function(){

		var modelo = $("#filtro").val();

		req = $.ajax({
			url : "/graficos",
			type : "POST",
			data : {modelo : modelo}
		});

		req.done(function(data){

			FusionCharts.ready(function () {
			    var myChart = new FusionCharts({
			        
			        type: 'line',
			        renderAt: 'grafico-container',
			        dataFormat: 'json',
			        dataSource: {
			            chart: {
			                caption: "Tabela FIPE",
					        xAxisName: "Data",
					        yAxisName: "Preço",
					        theme: "fusion"
			            },
			            
			            data:[
			            {
			                label: "Fevereiro",
			                value: data['precos'][0]
			            },
			            {
			                label: "Março",
			                value: data['precos'][1]
			            },
			            {
			                label: "Abril",
			                value: data['precos'][2]
			            },
			            {
			                label: "Maio",
			                value: data['precos'][3]
			            },
			            {
			                label: "Junho",
			                value: data['precos'][4]
			            }]
			        }
			    });

			    myChart.render();
			});

		});
	});
});