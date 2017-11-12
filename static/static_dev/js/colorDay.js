lessTimer();
function lessTimer(){
	var date = new Date();
		dayofweek = date.getDay();
		hours = date.getHours();
		minutes = date.getMinutes();

	for(var i = 1; i < 6; i++) {
        if (dayofweek == i && hours < 15) {
            // Закраска всього робочого дня
            for (i = 1; i < 8; i++) {
                $('tr').eq(1).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(i).find('td').eq(dayofweek).addClass('now_week');
            }

            // ПЕРШИЙ УРОК
            if ((hours == 8 && minutes >= 30) || (hours == 9 && minutes <= 15)) {
                $('tr').eq(1).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(1).find('td').eq(dayofweek).addClass('now_lesson')

            }
            // ПЕРША ПЕРЕРВА
            else if ((hours == 9 && minutes > 15) && (hours == 9 && minutes < 25)) {
                $('tr').eq(1).find('td').eq(dayofweek).removeClass('now_lesson');
                $('tr').eq(2).find('td').eq(dayofweek).addClass('next_lesson');
            }
            // ДРУГИЙ УРОК
            else if ((hours == 9 && minutes >= 25) || (hours == 10 && minutes <= 10)) {
                $('tr').eq(2).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(2).find('td').eq(dayofweek).addClass('now_lesson');
            }
            // ДРУГА ПЕРЕРВА
            else if ((hours == 10 && minutes > 10) && (hours == 10 && minutes < 30)) {
                $('tr').eq(2).find('td').eq(dayofweek).removeClass('now_lesson');
                $('tr').eq(3).find('td').eq(dayofweek).addClass('next_lesson');
            }
            // ТРЕТІЙ УРОК
            else if ((hours == 10 && minutes >= 30) || (hours == 11 && minutes <= 15)) {
                $('tr').eq(3).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(3).find('td').eq(dayofweek).addClass('now_lesson');
            }
            // ТРЕТЯ ПЕРЕРВА
            else if ((hours == 11 && minutes > 15) && (hours == 11 && minutes < 25)) {
                $('tr').eq(3).find('td').eq(dayofweek).removeClass('now_lesson');
                $('tr').eq(4).find('td').eq(dayofweek).addClass('next_lesson');
            }
            // ЧЕТВЕРТИЙ УРОК
            else if ((hours == 11 && minutes >= 25) || (hours == 12 && minutes <= 10)) {
                $('tr').eq(4).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(4).find('td').eq(dayofweek).addClass('now_lesson');
            }
            // ЧЕТВЕРТА ПЕРЕРВА
            else if ((hours == 12 && minutes > 10) && (hours == 12 && minutes < 30)) {
                $('tr').eq(4).find('td').eq(dayofweek).removeClass('now_lesson');
                $('tr').eq(5).find('td').eq(dayofweek).addClass('next_lesson');
            }
            // П'ЯТИЙ УРОК
            else if ((hours == 12 && minutes >= 30) || (hours == 13 && minutes <= 15)) {
                $('tr').eq(5).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(5).find('td').eq(dayofweek).addClass('now_lesson')
            }
            // П'ЯТА ПЕРЕРВА
            else if ((hours == 13 && minutes > 15) && (hours == 13 && minutes < 25)) {
                $('tr').eq(5).find('td').eq(dayofweek).removeClass('now_lesson');
                $('tr').eq(6).find('td').eq(dayofweek).addClass('next_lesson');
            }
            // ШОСТИЙ УРОК
            else if ((hours == 13 && minutes >= 25) || (hours == 14 && minutes <= 10)) {
                $('tr').eq(6).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(6).find('td').eq(dayofweek).addClass('now_lesson')
            }
            // ШОСТА ПЕРЕРВА
            else if ((hours == 14 && minutes > 10) && (hours == 14 && minutes < 20)) {
                $('tr').eq(6).find('td').eq(dayofweek).removeClass('now_lesson');
                $('tr').eq(7).find('td').eq(dayofweek).addClass('next_lesson');
            }
            // СЬОМИЙ УРОК
            else if (hours == 14 && minutes >= 20) {
                $('tr').eq(7).find('td').eq(dayofweek).removeClass('next_lesson');
                $('tr').eq(7).find('td').eq(dayofweek).addClass('now_lesson')
            }
		}
		// КІНЕЦЬ РОБОЧГО ДНЯ
		else if (dayofweek <= 5 && hours >= 15) {
			$('tr').eq(7).find('td').eq(dayofweek).removeClass('now_lesson');
			for (i = 1; i < 8; i++) {$('tr').eq(i).find('td').eq(dayofweek).removeClass('now_week')}
			$('tr').eq(1).find('td').eq(dayofweek + 1).addClass('next_lesson');

		}

		else if (dayofweek == 6 || dayofweek == 0) {
			$('tr').eq(1).find('td').eq(1).addClass('next_lesson')
		}

    }setTimeout(lessTimer, 250);
};
