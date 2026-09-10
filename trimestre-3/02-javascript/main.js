/* =========================================================================
   

    09/09/2026: Momento de codificación de esto

    


    JavaScript · Sencillo y Sintaxis Básica
    Lógica interactiva de la página de ejercicios (modales + inputs)




   ========================================================================= */

(function () {
  'use strict';

  /* Helpers ------------------------------------------------------------- */
  const $  = (id) => document.getElementById(id);
  const fmt = (n) => Number(n).toLocaleString('es-CO');

  /* =====================================================================
     1) POP-UP DE BIENVENIDA
     Se muestra al renderizar la página y se cierra tras 4 segundos.
     ===================================================================== */
  function initWelcome() {
    const el = $('welcomeModal');
    if (!el || typeof bootstrap === 'undefined') return;

    const modal = new bootstrap.Modal(el, { backdrop: 'static', keyboard: false });
    modal.show();

    const bar = $('welcomeProgress');
    if (bar) {
      bar.style.transition = 'none';
      bar.style.width = '0%';
      // Fuerza reflow para reiniciar la animación
      void bar.offsetWidth;
      requestAnimationFrame(() => {
        bar.style.transition = 'width 4000ms linear';
        bar.style.width = '100%';
      });
    }

    window.setTimeout(() => modal.hide(), 4000);
  }

  /* =====================================================================
     2) EJERCICIO 1 · Condicionales if / else
     ===================================================================== */
  function initEj1() {
    const btn = $('ej1-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const dinero = parseFloat($('ej1-dinero').value);
      const precio = parseFloat($('ej1-precio').value);
      const out    = $('ej1-result');

      if (isNaN(dinero) || isNaN(precio)) {
        out.className = 'result-box result-error';
        out.innerHTML = '<i class="bi bi-exclamation-triangle"></i> Debes ingresar ambos valores numéricos.';
        return;
      }

      if (dinero >= precio) {
        out.className = 'result-box result-ok';
        out.innerHTML =
          `Tienes $${fmt(dinero)} y el producto cuesta $${fmt(precio)}.<br>` +
          '<strong>¡Puedes comprar el producto!</strong>';
      } else {
        out.className = 'result-box result-error';
        out.innerHTML =
          `Tienes $${fmt(dinero)} y el producto cuesta $${fmt(precio)}.<br>` +
          '<strong>No tienes suficiente dinero para comprarlo.</strong>';
      }
    });
  }

  /* =====================================================================
     3) EJERCICIO 2 · Bucles y arreglos (for + filter)
     ===================================================================== */
  function initEj2() {
    const btn = $('ej2-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const numeros = [];
      let suma = 0;

      for (let i = 1; i <= 10; i++) {
        numeros.push(i);
        suma += i;
      }

      const pares = numeros.filter((n) => n % 2 === 0);

      const out = $('ej2-result');
      out.className = 'result-box result-ok';
      out.innerHTML =
        `<strong>Arreglo generado:</strong> [${numeros.join(', ')}]<br>` +
        `<strong>Suma total (1 al 10):</strong> ${suma}<br>` +
        `<strong>Números pares (filter):</strong> [${pares.join(', ')}]`;
    });
  }

  /* =====================================================================
     4) EJERCICIO 3 · Funciones con parámetros
     ===================================================================== */
  function evaluarNota(nota) {
    if (nota < 3) return 'Reprobado';
    if (nota >= 3 && nota < 4) return 'Aprobado';
    return 'Excelente';
  }

  function initEj3() {
    const btn = $('ej3-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const nota = parseFloat($('ej3-nota').value);
      const out  = $('ej3-result');

      if (isNaN(nota)) {
        out.className = 'result-box result-error';
        out.innerHTML = '<i class="bi bi-exclamation-triangle"></i> Ingresa una nota numérica.';
        return;
      }

      const resultado = evaluarNota(nota);
      out.className = 'result-box result-ok';
      out.innerHTML = `evaluarNota(${nota}) → <strong>${resultado}</strong>`;
    });
  }

  /* =====================================================================
     5) EJERCICIO 4 · switch (calificación cualitativa)
     ===================================================================== */
  function initEj4() {
    const btn = $('ej4-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const nota = parseInt($('ej4-nota').value, 10);
      const out  = $('ej4-result');
      let resultado;

      switch (nota) {
        case 1: resultado = 'Deficiente';  break;
        case 2: resultado = 'Insuficiente'; break;
        case 3: resultado = 'Aceptable';   break;
        case 4: resultado = 'Sobresaliente'; break;
        case 5: resultado = 'Excelente';   break;
        default: resultado = 'Nota no válida, debe estar entre 1-5';
      }

      out.className = 'result-box result-ok';
      out.innerHTML = `Calificación cualitativa: <strong>${resultado}</strong>`;
    });
  }

  /* =====================================================================
     6) EJERCICIO 5 · while (suma del 1 al 10)
     ===================================================================== */
  function initEj5() {
    const btn = $('ej5-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      let numero = 1;
      let suma = 0;
      const pasos = [];

      while (numero <= 10) {
        suma = suma + numero;
        pasos.push(`Iteración ${numero}: suma = ${suma}`);
        numero = numero + 1;
      }

      const out = $('ej5-result');
      out.className = 'result-box result-ok';
      out.innerHTML =
        pasos.map((p) => `<div class="step-line">${p}</div>`).join('') +
        `<hr><strong>Resultado final de la suma: ${suma}</strong>`;
    });
  }

  /* =====================================================================
     7) EJERCICIO 6 · Números pares del 1 al 10
     ===================================================================== */
  function initEj6() {
    const btn = $('ej6-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const pares = [];
      for (let i = 1; i <= 10; i++) {
        if (i % 2 === 0) pares.push(i);
      }

      const out = $('ej6-result');
      out.className = 'result-box result-ok';
      out.innerHTML = `Números pares encontrados: <strong>[${pares.join(', ')}]</strong>`;
    });
  }

  /* =====================================================================
     8) EJERCICIO 7 · Arrow function (promedio)
     ===================================================================== */
  const promedio = (a, b, c) => (a + b + c) / 3;

  function initEj7() {
    const btn = $('ej7-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const n1 = parseFloat($('ej7-n1').value);
      const n2 = parseFloat($('ej7-n2').value);
      const n3 = parseFloat($('ej7-n3').value);
      const out = $('ej7-result');

      if ([n1, n2, n3].some((n) => isNaN(n))) {
        out.className = 'result-box result-error';
        out.innerHTML = '<i class="bi bi-exclamation-triangle"></i> Debes ingresar las tres notas.';
        return;
      }

      const resultado = promedio(n1, n2, n3);
      out.className = 'result-box result-ok';
      out.innerHTML = `promedio(${n1}, ${n2}, ${n3}) → <strong>${resultado.toFixed(2)}</strong>`;
    });
  }

  /* =====================================================================
     9) EJERCICIO 8 · Factura hielo seco
        Descuentos por tipo de cliente:
        1 → 5%  |  2 → 8%  |  3 → 12%  |  4 → 15%
     ===================================================================== */
  const TASAS = { 1: 0.05, 2: 0.08, 3: 0.12, 4: 0.15 };

  function initEj8() {
    const btn = $('ej8-btn');
    if (!btn) return;

    btn.addEventListener('click', () => {
      const out      = $('ej8-result');
      const nombre   = $('ej8-nombre').value.trim() || 'Cliente sin nombre';
      const tipo     = parseInt($('ej8-tipo').value, 10);
      const cantidad = parseInt($('ej8-cantidad').value, 10);
      const valor    = parseFloat($('ej8-valor').value);

      if (isNaN(tipo) || isNaN(cantidad) || isNaN(valor) || cantidad <= 0 || valor <= 0) {
        out.className = 'result-box result-error';
        out.innerHTML = '<i class="bi bi-exclamation-triangle"></i> Verifica los datos: tipo (1-4), cantidad y valor deben ser válidos.';
        return;
      }

      const subtotal  = cantidad * valor;
      const tasa      = TASAS[tipo] || 0;
      const descuento = subtotal * tasa;
      const neto      = subtotal - descuento;

      out.className = 'result-box result-ok';
      out.innerHTML = `
        <div class="factura-line"><span>Cliente:</span><strong>${nombre}</strong></div>
        <div class="factura-line"><span>Tipo de cliente:</span><strong>${tipo} (${(tasa * 100).toFixed(0)}% descuento)</strong></div>
        <div class="factura-line"><span>Subtotal (${cantidad} × ${fmt(valor)}):</span><strong>${fmt(subtotal)}</strong></div>
        <div class="factura-line"><span>Descuento aplicado:</span><strong>- ${fmt(descuento)}</strong></div>
        <div class="factura-line total"><span>Neto por pagar:</span><strong>${fmt(neto)} u.m.</strong></div>
      `;
    });
  }

  /* =====================================================================
     UTILIDADES: botón "ir arriba" y año en el footer
     ===================================================================== */
  function initMisc() {
    const toTop = $('toTop');
    if (toTop) {
      window.addEventListener('scroll', () => {
        toTop.classList.toggle('visible', window.scrollY > 420);
      });
      toTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
      });
    }

    const yearEl = $('year');
    if (yearEl) yearEl.textContent = new Date().getFullYear();
  }

  /* =====================================================================
     BOOT
     ===================================================================== */
  function boot() {
    initWelcome();
    initEj1();
    initEj2();
    initEj3();
    initEj4();
    initEj5();
    initEj6();
    initEj7();
    initEj8();
    initMisc();

    if (window.AOS)   AOS.init({ duration: 800, once: true, offset: 90, easing: 'ease-out-cubic' });
    if (window.Prism) Prism.highlightAll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();