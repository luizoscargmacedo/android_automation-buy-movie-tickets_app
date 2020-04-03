# android_automation-buy-movie-tickets_app

**Project:** buy-movie-tickets <br>
**Description:** Feature automation to valide all operations <br>
**Version:** 1.0 <br>
**Created:** 2020-02-16
<br><br>




### Environment Configuration ###

  ### Install ###

 **Python**
   - url: https://www.python.org/downloads/

 **Pip**   
   - url: https://pip.pypa.io/en/stable/installing/

 **Android Studio**  
   - url: https://developer.android.com/studio

**Allure Report**
  - url: https://docs.qameta.io/allure/#_installing_a_commandline




### Configuration Project ###

  ## Created environment variable

**Android Studio**
  - export ANDROID_HOME=/Users/<userprofilehere>/Library/Android/sdk
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/build-tools/29.0.2"
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/platform-tools"
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/emulator"
  - export PATH=$PATH:/Library/Java/JavaVirtualMachines/jdk1.8.0_231.jdk/Contents/Home
  - export PATH=$PATH:"$PWD":"$ANDROID_HOME/tools/bin"

**Project Information** <br>
   **behave.yml** <br>
     - "environment": Environment to execute your test (dev, qa, cert, prod)<br>
     - "os": System Mobile (iOS or Android)<br>

    *service > capabilities*
     -  "android":
            "platformName": "Operation System Mobile"
            "platformVersion": "Version Operation System Mobile"
            "udid": "Id device real"
            "automationName": "uiautomator2"
            "deviceName": "Define name for device"
            "app": "Name apk or ipa, located in folder service > binary"


## Install Dependency ##
   **Command Line:** <br>
      - pip3 install -r requirements.txt

## Execution Project ##
    **Allure Report**
      - All Scenarios:
          - `behave -f allure_behave.formatter:AllureFormatter -o reports/allure_report *.feature`

      - By Tag:
          - `behave -f allure_behave.formatter:AllureFormatter -o reports/allure_report -t @nametag`





**E-mail:** luiz.gmacedo@gmail.com
