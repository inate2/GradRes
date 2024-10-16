// ページが読み込まれたときにタイマーを開始
window.onload = function() {
  // 制限時間（秒）
  const timeLimit = 10; // 例: 2分 = 120秒

  // 残り時間を表示するための要素を取得
  const timerElement = document.getElementById('timer');

  // タイマーのカウントダウンを開始
  let timeRemaining = timeLimit;
  const countdownInterval = setInterval(function() {
      // 分と秒に変換
      const minutes = Math.floor(timeRemaining / 60);
      const seconds = timeRemaining % 60;

      // 2桁表示を保つためにゼロ埋め
      const displayMinutes = minutes < 10 ? '0' + minutes : minutes;
      const displaySeconds = seconds < 10 ? '0' + seconds : seconds;

      // タイマーの表示を更新
      timerElement.textContent = `${displayMinutes}:${displaySeconds}`;

      // 時間を減少
      timeRemaining--;

      // タイマーがゼロになったらページを遷移
      if (timeRemaining < 0) {
          clearInterval(countdownInterval);
          window.location.href = "g1_page_1_3.html";
      }
  }, 1000); // 1秒ごとに実行
};