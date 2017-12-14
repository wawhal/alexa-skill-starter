# Alexa with Yoda quotes

This is an alexa skill which gives you a Yoda quote when you ask for it. This skill service gets deployed in four commands. (Make sure you have [hasura-cli](https://docs.hasura.io/0.15/manual/install-hasura-cli.html))

```
$ hasura quickstart /alexa-yoda-bot
$ cd alexa-yoda-bot
$ git add . && git commit -m "Initial Commit"
$ git push hasura master
```

This is a good place to start if you want to start developing Alexa Skills.

To link it with your Amazon Echo Device, go to your [Amazon developer console](https://developer.amazon.com/edw/home.html#/skills).

1. Create a new skill. Call it `Yoda Quote`. Give the invocation name as `qoda quote`. Click next.

2. Add this intent schema
```
{
  "intents": [
    {
      "intent": "YesIntent"
    },
    {
      "intent": "NoIntent"
    }
  ]
}
```

	Leave custom slot types empty
	Add the following sample utterances

```
YesIntent yes
YesIntent sure
YesIntent yeah
YesIntent ok

NoIntent no
NoIntent no thanks
NoIntent nope
```
	Click next.

3. For the service endpoint, check the `HTTPS` radio button.

	Put the default URL as `https://bot.<cluster-name>.hasura-app.io/yoda_quotes`. (Run `$ hasura cluster status` from root directory to know your cluster name).

	**Note**: For quick testing, we have one skill service live at https://bot.dedication76.hasura-app.io/yoda_quotes. (This test service will work only if you have followed 1 and 2)

	Click next.

4. About SSL certificates, Hasura services have auto generated `LetsEncrypt` Grade A SSL certificates. This means, you have to check the radio button that says `My development endpoint has a certificate from a trusted certificate authority`

	Click next.

5. Your skill is live on the ECHO device associated with your account. Test it by saying **Alexa**, `load yoda quote`. And Alexa will give you *Yoda* wisdom :)

