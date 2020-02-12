function getFormatDateBefore(dateBefore, dateNumber){
    var year = dateBefore.getFullYear();
    var month = (1 + dateBefore.getMonth());
    month = month >= 10 ? month : '0' + month;
    var day = dateBefore.getDate();
    day = day >= 10 ? day : '0' + day;
    day = day - dateNumber;

    return  year + '-' + month + '-' + day;
}