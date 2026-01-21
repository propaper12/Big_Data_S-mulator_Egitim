# 🏗️ Big Data Architecture Studio

> **Teoriden Pratiğe:** Python ve Streamlit kullanarak modern Büyük Veri Mimarilerini tasarlamak, doğrulamak ve simüle etmek için geliştirdiğim interaktif Ar-Ge laboratuvarı.

![Durum](https://img.shields.io/badge/Durum-Aktif-success)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31%2B-red)

## 📖 Proje Hakkında

Veri Mühendisliği yolculuğuma başladığımda, **Kafka, Spark, Flink ve Kubernetes** gibi araçların sözdizimini (syntax) öğrenmenin ötesinde, bu parçaların **birbiriyle nasıl uyum içinde çalıştığını** anlamanın çok daha zor olduğunu fark ettim.

Bu projeyi, öğrenme sürecimi hızlandırmak ve kendime ait bir **"Dijital Not Defteri"** oluşturmak amacıyla geliştirdim.

**Bu platform sayesinde:**
1.  Karmaşık mimari bağımlılıkları **görselleştiriyorum**.
2.  Gerçek dünya senaryolarını (Lambda, Kappa, Lakehouse) **simüle ediyorum**.
3.  Mantıksal hataları (Örn: Kafka seçip Zookeeper eklememek) **doğruluyorum**.
4.  Altyapı kodlarını (Terraform/Docker) **otomatik üretiyorum**.

Bu sadece bir çizim aracı değil; Veri Mimarı olma yolunda ilerleyenler için yaşayan bir rehberdir.

## 🚀 Özellikler

* **📚 Canlı Teknoloji Envanteri:** 30'dan fazla Büyük Veri teknolojisi için detaylı akademik açıklamalar, kullanım senaryoları ve "Hello World" kod örnekleri.
* **🎨 Akıllı Simülatör:** Sürükle-bırak mantığıyla çalışan, Graphviz destekli otomatik mimari çizim motoru.
* **🛡️ Mantıksal Doğrulama:** Uyumsuz bileşenleri tespit eden ve mimari hataları engelleyen kural motoru.
* **🏗️ Altyapı Farkındalığı (Infrastructure Aware):** Seçilen servislerin Kubernetes, Docker veya YARN üzerinde nasıl konumlandığını otomatik olarak katmanlar halinde gösterir.

## 🛠️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1.  **Repoyu Klonlayın**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/BigDataSimulator.git](https://github.com/KULLANICI_ADINIZ/BigDataSimulator.git)
    cd BigDataSimulator
    ```

2.  **Gereksinimleri Yükleyin**
    ```bash
    pip install -r requirements.txt
    ```
    *(Not: Diyagramların çizilebilmesi için işletim sisteminizde [Graphviz](https://graphviz.org/download/) yüklü olmalıdır.)*

3.  **Uygulamayı Başlatın**
    ```bash
    streamlit run Home.py
    ```

## 📸 Ekran Görüntüleri

*(Buraya uygulamanın ekran görüntülerini veya GIF'ini ekleyebilirsiniz)*

## 🤝 Katkıda Bulunma

Bu proje benim öğrenme sürecimin bir yansımasıdır. Eğer eksik bir teknoloji görürseniz veya daha iyi bir mimari öneriniz varsa, katkıda bulunmaktan çekinmeyin!

1.  Projeyi Fork'layın
2.  Yeni bir Branch oluşturun (`git checkout -b feature/YeniOzellik`)
3.  Değişikliklerinizi Commit'leyin (`git commit -m 'Yeni teknoloji eklendi: Redpanda'`)
4.  Branch'inizi Push'layın (`git push origin feature/YeniOzellik`)
5.  Bir Pull Request oluşturun

## 👤 İletişim

**[Adınız Soyadınız]**

* LinkedIn: [Profil Linkiniz]
* GitHub: [@KullaniciAdiniz]

---
*Bu proje ❤️ ile Python ve Streamlit kullanılarak geliştirilmiştir.*
