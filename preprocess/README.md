This directory contain utilities to preprocess the source code into images.

`gather.py` goes through given directories, finds all files matching specified suffix, 
and concatenates them into new file at given location.

`render.py` takes name of the bundle created by `gather.py` and creates given number of images,
sampled at random locations in the bundle.


The commands to create the data in this repo were:

```bash
python gather.py ../data/bundle-c.txt .c \
  ../data/sources/c/FFmpeg-master/libavdevice \
  ../data/sources/c/FFmpeg-master/libpostproc \
  ../data/sources/c/curl-master/src \
  ../data/sources/c/git-master/builtin \
  ../data/sources/c/goaccess-master/src \
  ../data/sources/c/nuklear-master/src \
  ../data/sources/c/the_silver_searcher-master/src

python gather.py ../data/bundle-cpp.txt .cpp \
  ../data/sources/cpp/cpprestsdk-master/Release/src \
  ../data/sources/cpp/cpprestsdk-master/Release/samples/BlackJack \
  ../data/sources/cpp/libtorrent-master/src \
  ../data/sources/cpp/openage-master/libopenage \
  ../data/sources/cpp/openpose-master/src \
  ../data/sources/cpp/solidity-develop/libsolidity \
  ../data/sources/cpp/tinyrenderer-master \
  ../data/sources/cpp/yuzu-master/src/core

python gather.py ../data/bundle-csharp.txt .cs \
  ../data/sources/csharp/CodeHub-master \
  ../data/sources/csharp/Nancy-master/src/Nancy \
  ../data/sources/csharp/OpenRA-bleed/OpenRA.Game \
  ../data/sources/csharp/SignalR-master/src/Microsoft.AspNet.SignalR.Core \
  ../data/sources/csharp/choco-master/src/chocolatey \
  ../data/sources/csharp/coreclr-master/src/System.Private.CoreLib/src/System/Threading \
  ../data/sources/csharp/shadowsocks-windows-master/shadowsocks-csharp

python gather.py ../data/bundle-java.txt .java \
  ../data/sources/java/retrofit-master \
  ../data/sources/java/okhttp-master/okhttp \
  ../data/sources/java/guava-master/guava/src/com/google/common/collect \
  ../data/sources/java/fastjson-master/src/main \
  ../data/sources/java/elasticsearch-master/client/rest-high-level/src/main \
  ../data/sources/java/RxJava-2.x/src/main/java/io/reactivex

python gather.py ../data/bundle-python.txt .py \
  ../data/sources/python/certbot-master/certbot \
  ../data/sources/python/django-master/django/core \
  ../data/sources/python/django-master/django/utils \
  ../data/sources/python/flask-master/flask \
  ../data/sources/python/httpie-master/httpie \
  ../data/sources/python/keras-master/keras \
  ../data/sources/python/requests-master/requests \
  ../data/sources/python/scrapy-master/scrapy \
  ../data/sources/python/thefuck-master/thefuck

python gather.py ../data/bundle-ruby.txt .rb \
  ../data/sources/ruby/brew-master/Library/Homebrew/cask \
  ../data/sources/ruby/brew-master/Library/Homebrew/cmd \
  ../data/sources/ruby/capistrano-master/lib \
  ../data/sources/ruby/discourse-master/lib \
  ../data/sources/ruby/gitlabhq-master/lib/gitlab \
  ../data/sources/ruby/jekyll-master/lib/jekyll \
  ../data/sources/ruby/rails-master/activesupport/lib/active_support \
  ../data/sources/ruby/sinatra-master/lib \
  ../data/sources/ruby/vagrant-master/lib

python gather.py ../data/bundle-rust.txt .rs \
  ../data/sources/rust/alacritty-master/src \
  ../data/sources/rust/bat-master \
  ../data/sources/rust/coreutils-master/src \
  ../data/sources/rust/exa-master/src \
  ../data/sources/rust/fd-master \
  ../data/sources/rust/servo-master/components/canvas \
  ../data/sources/rust/servo-master/components/hashglobe \
  ../data/sources/rust/yew-master/src

python gather.py ../data/bundle-go.txt .go \
  ../data/sources/go/etcd-master/etcdserver \
  ../data/sources/go/gin-master \
  ../data/sources/go/go-ethereum-master/swarm \
  ../data/sources/go/go-master/src/cmd/go \
  ../data/sources/go/gogs-master/models \
  ../data/sources/go/hugo-master/hugolib \
  ../data/sources/go/moby-master/daemon \
  ../data/sources/go/syncthing-master/lib/model


python render.py ../data/bundle-c.txt 500 ../data/renders/c/
python render.py ../data/bundle-cpp.txt 500 ../data/renders/cpp/
python render.py ../data/bundle-csharp.txt 500 ../data/renders/csharp/
python render.py ../data/bundle-go.txt 500 ../data/renders/go/
python render.py ../data/bundle-java.txt 500 ../data/renders/java/
python render.py ../data/bundle-python.txt 500 ../data/renders/python/
python render.py ../data/bundle-ruby.txt 500 ../data/renders/ruby/
python render.py ../data/bundle-rust.txt 500 ../data/renders/rust/
```
