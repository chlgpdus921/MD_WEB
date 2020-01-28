 $(function () {

      /*
     * BAR CHART
     * ---------
     */

    var bar_data = {
      data : [['bad ball joint', 10], ['bad brake pad', 8], ['engine running without oil+engine seizing up', 4],
      ['failing water pump', 13], ['hole in muffler', 17], ['normal', 9]],
      color: '#3c8dbc'
    }
    $.plot('#bar-chart', [bar_data], {
      grid  : {
        borderWidth: 1,
        borderColor: '#f3f3f3',
        tickColor  : '#f3f3f3'
      },
      series: {
        bars: {
          show    : true,
          barWidth: 0.5,
          align   : 'center'
        }
      },
      xaxis : {
        mode      : 'categories',
        tickLength: 0
      }
    })
    /* END BAR CHART */

    /*
     * DONUT CHART
     * -----------
     */
    var donutData = [
      { label: '', data: 10, color: '#56a0f0' },
      { label: '', data: 20, color: '#0073b7' },
      { label: '', data: 30, color: '#56c4f0' },
      { label: '', data: 40, color: '#414c9a' },
      { label: '', data: 50, color: '#6756f0' },
      { label: '', data: 60, color: '#9f56f0' }
    ]
    $.plot('#donut-chart', donutData, {
      series: {
        pie: {
          show       : true,
          radius     : 1,
          innerRadius: 0.5,
          label      : {
            show     : true,
            radius   : 2 / 3,
            formatter: labelFormatter,
            threshold: 0.1
          }

        }
      },
      legend: {
        show: false
      }
    })
    /*
     * END DONUT CHART
     */

  })

  /*
   * Custom Label formatter
   * ----------------------
   */
  function labelFormatter(label, series) {
    return '<div style="font-size:13px; text-align:center; padding:2px; color: #fff; font-weight: 600;">'
      + label
      + '<br>'
      + Math.round(series.percent) + '%</div>'
  }
