/* Reusable quiz component, shared by all lessons.
 *
 * Markup contract:
 *   <div class="q" data-answer="1">
 *     <p class="stem">…</p>
 *     <button>option 0</button>
 *     <button>option 1</button>
 *     <p class="why" hidden>explanation shown after answering</p>
 *   </div>
 *
 * Answering is one click and feedback is immediate: the point is retrieval
 * practice, so the explanation is only revealed once a choice is committed.
 */
(function () {
  function wire(q) {
    var correct = Number(q.dataset.answer);
    var buttons = Array.prototype.slice.call(q.querySelectorAll('button'));
    var why = q.querySelector('.why');

    buttons.forEach(function (button, index) {
      button.addEventListener('click', function () {
        buttons.forEach(function (b, i) {
          b.disabled = true;
          if (i === correct) b.classList.add('right');
        });
        if (index !== correct) button.classList.add('wrong');
        if (why) why.hidden = false;
        q.dataset.answered = index === correct ? 'right' : 'wrong';
      });
    });
  }

  document.querySelectorAll('.q').forEach(wire);
})();
