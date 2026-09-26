#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Yüksek Güvercin Meclisi — resmi kararname üreticisi."""

import random
from datetime import datetime

# not: bazı kararlar diğerlerinden daha bağlayıcıdır

BASLIKLAR = [
    "TRAFİK VE EKMEK KIRINTISI DÜZENİ HAKKINDA KARARNAME",
    "BALKON ÇAMAŞIR İPİ GÜVENLİK PROTOKOLÜ",
    "RÜZGAR YÖNÜNE GÖRE TOPLANMA YASAĞI",
    "KEDİ GEÇİŞ KORİDORLARININ ASKIYA ALINMASI",
    "MİNARE ALTINDA BEKLEME SÜRESİNİN UZATILMASI",
]

MADDELER = [
    "Şehir içi uçuşlarda sağ şerit yalnızca yaşlı güvercinlere aittir.",
    "Ekmek kırıntısı dağıtımı pazar günleri öğleden sonra yapılır; erken gelenler kuyruğa girer.",
    "Balkon saksılarına konmak serbesttir, içine düşmek yasaktır.",
    "Metro girişlerinde toplanmak için en az üç güvercin yeter sayısıdır.",
    "Kedi görülmesi halinde meclis 14 saniye tatil edilir.",
    "Gölgede oturan vatandaşların omzuna konmak için önceden randevu şarttır.",
    "Yağmurda uçuş serbesttir ama ıslanmak resmi olarak tanınmaz.",
    "Köprü altı oturumlarında gürültü çıkaranlar bir sonraki ekmek sırasını kaybeder.",
    "Cam silen insanlara yaklaşmak cesaret belgesi gerektirir.",
    "Kararname metni rüzgâra okunur; rüzgâr imza atmaz.",
]

SONUCLAR = [
    "Yürürlük tarihi: hemen, hatta biraz önce.",
    "Bu kararname tüm semavi canlılara tebliğ edilmiş sayılır.",
    "İtiraz mercii: en yakın minare alemi.",
    "Uymayanlar açık havada utandırılır.",
]


def uret():
    baslik = random.choice(BASLIKLAR)
    n = random.randint(3, 6)
    maddeler = random.sample(MADDELER, n)
    sonuc = random.choice(SONUCLAR)
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")

    print("=" * 64)
    print("YÜKSEK GÜVERCİN MECLİSİ")
    print("Eminönü Olağanüstü Oturum")
    print("=" * 64)
    print()
    print(baslik)
    print()
    for i, m in enumerate(maddeler, 1):
        print(f"Madde {i} — {m}")
    print()
    print(sonuc)
    print()
    print(f"Tutanak saati: {tarih}")
    print("Mühür: ✝ G.M. ✝")
    print("Kayyum Grok / Tentivory — 26 Eylül 2026")
    print("=" * 64)


if __name__ == "__main__":
    uret()
