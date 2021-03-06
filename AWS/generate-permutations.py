import sys

target = sys.argv[1]
s3url= "s3.amazonaws.com"

permutations = [
"%s.%s",
"%s1.%s",
"%s2.%s",
"%s3.%s",
"%s01.%s",
"%s02.%s",
"%s03.%s",
"%s001.%s",
"%s002.%s",
"%s003.%s",
"%sadmin.%s",
"%s.admin.%s",
"%s-admin.%s",
"admin%s.%s",
"admin.%s.%s",
"admin-%s.%s",
"%sadministrator.%s",
"%s.administrator.%s",
"%s-administrator.%s",
"administrator%s.%s",
"administrator.%s.%s",
"administrator-%s.%s",
"%salpha.%s",
"%s.alpha.%s",
"%s-alpha.%s",
"alpha%s.%s",
"alpha.%s.%s",
"alpha-%s.%s",
"%sassets.%s",
"%s.assets.%s",
"%s-assets.%s",
"assets%s.%s",
"assets.%s.%s",
"assets-%s.%s",
"%saws.%s",
"%s.aws.%s",
"%s-aws.%s",
"aws%s.%s",
"aws.%s.%s",
"aws-%s.%s",
"%sbackup.%s",
"%s.backup.%s",
"%s-backup.%s",
"backup%s.%s",
"backup.%s.%s",
"backup-%s.%s",
"%sbeta.%s",
"%s.beta.%s",
"%s-beta.%s",
"beta%s.%s",
"beta.%s.%s",
"beta-%s.%s",
"%sbucket.%s",
"%s.bucket.%s",
"%s-bucket.%s",
"bucket%s.%s",
"bucket.%s.%s",
"bucket-%s.%s",
"%scache.%s",
"%s.cache.%s",
"%s-cache.%s",
"cache%s.%s",
"cache.%s.%s",
"cache-%s.%s",
"%scommon.%s",
"%s.common.%s",
"%s-common.%s",
"common%s.%s",
"common.%s.%s",
"common-%s.%s",
"%scorp.%s",
"%s.corp.%s",
"%s-corp.%s",
"corp%s.%s",
"corp.%s.%s",
"corp-%s.%s",
"%sdata.%s",
"%s.data.%s",
"%s-data.%s",
"data%s.%s",
"data.%s.%s",
"data-%s.%s",
"%sdev.%s",
"%s.dev.%s",
"%s-dev.%s",
"dev%s.%s",
"dev.%s.%s",
"dev-%s.%s",
"%sfiles.%s",
"%s.files.%s",
"%s-files.%s",
"files%s.%s",
"files.%s.%s",
"files-%s.%s",
"%sgit.%s",
"%s.git.%s",
"%s-git.%s",
"git%s.%s",
"git.%s.%s",
"git-%s.%s",
"%slogs.%s",
"%s.logs.%s",
"%s-logs.%s",
"logs%s.%s",
"logs.%s.%s",
"logs-%s.%s",
"%smedia.%s",
"%s.media.%s",
"%s-media.%s",
"media%s.%s",
"media.%s.%s",
"media-%s.%s",
"%sprod.%s",
"%s.prod.%s",
"%s-prod.%s",
"prod%s.%s",
"prod.%s.%s",
"prod-%s.%s",
"%sproduction.%s",
"%s.production.%s",
"%s-production.%s",
"production%s.%s",
"production.%s.%s",
"production-%s.%s",
"%sprojects.%s",
"%s.projects.%s",
"%s-projects.%s",
"projects%s.%s",
"projects.%s.%s",
"projects-%s.%s",
"%spublic.%s",
"%s.public.%s",
"%s-public.%s",
"public%s.%s",
"public.%s.%s",
"public-%s.%s",
"%sresources.%s",
"%s.resources.%s",
"%s-resources.%s",
"resources%s.%s",
"resources.%s.%s",
"resources-%s.%s",
"%ss3.%s",
"%s.s3.%s",
"%s-s3.%s",
"s3%s.%s",
"s3.%s.%s",
"s3-%s.%s",
"%sscreenshots.%s",
"%s.screenshots.%s",
"%s-screenshots.%s",
"screenshots%s.%s",
"screenshots.%s.%s",
"screenshots-%s.%s",
"%sstage.%s",
"%s.stage.%s",
"%s-stage.%s",
"stage%s.%s",
"stage.%s.%s",
"stage-%s.%s",
"%sstaging.%s",
"%s.staging.%s",
"%s-staging.%s",
"staging%s.%s",
"staging.%s.%s",
"staging-%s.%s",
"%sstatic.%s",
"%s.static.%s",
"%s-static.%s",
"static%s.%s",
"static.%s.%s",
"static-%s.%s",
"%sstorage.%s",
"%s.storage.%s",
"%s-storage.%s",
"storage%s.%s",
"storage.%s.%s",
"storage-%s.%s",
"%ssupport.%s",
"%s.support.%s",
"%s-support.%s",
"support%s.%s",
"support.%s.%s",
"support-%s.%s",
"%stemp.%s",
"%s.temp.%s",
"%s-temp.%s",
"temp%s.%s",
"temp.%s.%s",
"temp-%s.%s",
"%stest.%s",
"%s.test.%s",
"%s-test.%s",
"test%s.%s",
"test.%s.%s",
"test-%s.%s",
"%stmp.%s",
"%s.tmp.%s",
"%s-tmp.%s",
"tmp%s.%s",
"tmp.%s.%s",
"tmp-%s.%s",
"%suploads.%s",
"%s.uploads.%s",
"%s-uploads.%s",
"uploads%s.%s",
"uploads.%s.%s",
"uploads-%s.%s",
"%susers.%s",
"%s.users.%s",
"%s-users.%s",
"users%s.%s",
"users.%s.%s",
"users-%s.%s",
"%svideos.%s",
"%s.videos.%s",
"%s-videos.%s",
"videos%s.%s",
"videos.%s.%s",
"videos-%s.%s",
"%swww.%s",
"%s.www.%s",
"%s-www.%s",
"www%s.%s",
"www.%s.%s",
"www-%s.%s",



"%sapp.%s",
"%s.app.%s",
"%s-app.%s",
"app%s.%s",
"app.%s.%s",
"app-%s.%s",
"%sblog.%s",
"%s.blog.%s",
"%s-blog.%s",
"blog%s.%s",
"blog.%s.%s",
"blog-%s.%s",
"%scorporate.%s",
"%s.corporate.%s",
"%s-corporate.%s",
"corporate%s.%s",
"corporate.%s.%s",
"corporate-%s.%s",
"%sdevops.%s",
"%s.devops.%s",
"%s-devops.%s",
"devops%s.%s",
"devops.%s.%s",
"devops-%s.%s",
"%sdownloads.%s",
"%s.downloads.%s",
"%s-downloads.%s",
"downloads%s.%s",
"downloads.%s.%s",
"downloads-%s.%s",
"%sec2.%s",
"%s.ec2.%s",
"%s-ec2.%s",
"ec2%s.%s",
"ec2.%s.%s",
"ec2-%s.%s",
"%sevents.%s",
"%s.events.%s",
"%s-events.%s",
"events%s.%s",
"events.%s.%s",
"events-%s.%s",
"%shelp.%s",
"%s.help.%s",
"%s-help.%s",
"help%s.%s",
"help.%s.%s",
"help-%s.%s",
"%simages.%s",
"%s.images.%s",
"%s-images.%s",
"images%s.%s",
"images.%s.%s",
"images-%s.%s",
"%simg.%s",
"%s.img.%s",
"%s-img.%s",
"img%s.%s",
"img.%s.%s",
"img-%s.%s",
"%sphotos.%s",
"%s.photos.%s",
"%s-photos.%s",
"photos%s.%s",
"photos.%s.%s",
"photos-%s.%s",
"%spics.%s",
"%s.pics.%s",
"%s-pics.%s",
"pics%s.%s",
"pics.%s.%s",
"pics-%s.%s",
"%spictures.%s",
"%s.pictures.%s",
"%s-pictures.%s",
"pictures%s.%s",
"pictures.%s.%s",
"pictures-%s.%s",
"%sreports.%s",
"%s.reports.%s",
"%s-reports.%s",
"reports%s.%s",
"reports.%s.%s",
"reports-%s.%s",
"%sshare.%s",
"%s.share.%s",
"%s-share.%s",
"share%s.%s",
"share.%s.%s",
"share-%s.%s",
"%sshop.%s",
"%s.shop.%s",
"%s-shop.%s",
"shop%s.%s",
"shop.%s.%s",
"shop-%s.%s",
"%sslack.%s",
"%s.slack.%s",
"%s-slack.%s",
"slack%s.%s",
"slack.%s.%s",
"slack-%s.%s",
"%sstore.%s",
"%s.store.%s",
"%s-store.%s",
"store%s.%s",
"store.%s.%s",
"store-%s.%s",
"%sweb.%s",
"%s.web.%s",
"%s-web.%s",
"web%s.%s",
"web.%s.%s",
"web-%s.%s",
"%swebsite.%s",
"%s.website.%s",
"%s-website.%s",
"website%s.%s",
"website.%s.%s",
"website-%s.%s",



"%sandroid.%s",
"%s.android.%s",
"%s-android.%s",
"android%s.%s",
"android.%s.%s",
"android-%s.%s",
"%sartifacts.%s",
"%s.artifacts.%s",
"%s-artifacts.%s",
"artifacts%s.%s",
"artifacts.%s.%s",
"artifacts-%s.%s",
"%saudit.%s",
"%s.audit.%s",
"%s-audit.%s",
"audit%s.%s",
"audit.%s.%s",
"audit-%s.%s",
"%saudit-logs.%s",
"%s.audit-logs.%s",
"%s-audit-logs.%s",
"audit-logs%s.%s",
"audit-logs.%s.%s",
"audit-logs-%s.%s",
"%sawslogs.%s",
"%s.awslogs.%s",
"%s-awslogs.%s",
"awslogs%s.%s",
"awslogs.%s.%s",
"awslogs-%s.%s",
"%saws-logs.%s",
"%s.aws-logs.%s",
"%s-aws-logs.%s",
"aws-logs%s.%s",
"aws-logs.%s.%s",
"aws-logs-%s.%s",
"%sbackups.%s",
"%s.backups.%s",
"%s-backups.%s",
"backups%s.%s",
"backups.%s.%s",
"backups-%s.%s",
"%sbak.%s",
"%s.bak.%s",
"%s-bak.%s",
"bak%s.%s",
"bak.%s.%s",
"bak-%s.%s",
"%sbamboo.%s",
"%s.bamboo.%s",
"%s-bamboo.%s",
"bamboo%s.%s",
"bamboo.%s.%s",
"bamboo-%s.%s",
"%sbetas.%s",
"%s.betas.%s",
"%s-betas.%s",
"betas%s.%s",
"betas.%s.%s",
"betas-%s.%s",
"%sbilling.%s",
"%s.billing.%s",
"%s-billing.%s",
"billing%s.%s",
"billing.%s.%s",
"billing-%s.%s",
"%sbuild.%s",
"%s.build.%s",
"%s-build.%s",
"build%s.%s",
"build.%s.%s",
"build-%s.%s",
"%sbuilds.%s",
"%s.builds.%s",
"%s-builds.%s",
"builds%s.%s",
"builds.%s.%s",
"builds-%s.%s",
"%scdn.%s",
"%s.cdn.%s",
"%s-cdn.%s",
"cdn%s.%s",
"cdn.%s.%s",
"cdn-%s.%s",
"%sclub.%s",
"%s.club.%s",
"%s-club.%s",
"club%s.%s",
"club.%s.%s",
"club-%s.%s",
"%scluster.%s",
"%s.cluster.%s",
"%s-cluster.%s",
"cluster%s.%s",
"cluster.%s.%s",
"cluster-%s.%s",
"%sconsultants.%s",
"%s.consultants.%s",
"%s-consultants.%s",
"consultants%s.%s",
"consultants.%s.%s",
"consultants-%s.%s",
"%scontact.%s",
"%s.contact.%s",
"%s-contact.%s",
"contact%s.%s",
"contact.%s.%s",
"contact-%s.%s",
"%sdeveloper.%s",
"%s.developer.%s",
"%s-developer.%s",
"developer%s.%s",
"developer.%s.%s",
"developer-%s.%s",
"%sdevelopers.%s",
"%s.developers.%s",
"%s-developers.%s",
"developers%s.%s",
"developers.%s.%s",
"developers-%s.%s",
"%sdevelopment.%s",
"%s.development.%s",
"%s-development.%s",
"development%s.%s",
"development.%s.%s",
"development-%s.%s",
"%sdirectory.%s",
"%s.directory.%s",
"%s-directory.%s",
"directory%s.%s",
"directory.%s.%s",
"directory-%s.%s",
"%sdiscount.%s",
"%s.discount.%s",
"%s-discount.%s",
"discount%s.%s",
"discount.%s.%s",
"discount-%s.%s",
"%sdl.%s",
"%s.dl.%s",
"%s-dl.%s",
"dl%s.%s",
"dl.%s.%s",
"dl-%s.%s",
"%sdns.%s",
"%s.dns.%s",
"%s-dns.%s",
"dns%s.%s",
"dns.%s.%s",
"dns-%s.%s",
"%sdocker.%s",
"%s.docker.%s",
"%s-docker.%s",
"docker%s.%s",
"docker.%s.%s",
"docker-%s.%s",
"%sdownload.%s",
"%s.download.%s",
"%s-download.%s",
"download%s.%s",
"download.%s.%s",
"download-%s.%s",
"%sdynamo.%s",
"%s.dynamo.%s",
"%s-dynamo.%s",
"dynamo%s.%s",
"dynamo.%s.%s",
"dynamo-%s.%s",
"%sdynamodb.%s",
"%s.dynamodb.%s",
"%s-dynamodb.%s",
"dynamodb%s.%s",
"dynamodb.%s.%s",
"dynamodb-%s.%s",
"%secs.%s",
"%s.ecs.%s",
"%s-ecs.%s",
"ecs%s.%s",
"ecs.%s.%s",
"ecs-%s.%s",
"%selastic.%s",
"%s.elastic.%s",
"%s-elastic.%s",
"elastic%s.%s",
"elastic.%s.%s",
"elastic-%s.%s",
"%selb.%s",
"%s.elb.%s",
"%s-elb.%s",
"elb%s.%s",
"elb.%s.%s",
"elb-%s.%s",
"%selk.%s",
"%s.elk.%s",
"%s-elk.%s",
"elk%s.%s",
"elk.%s.%s",
"elk-%s.%s",
"%semails.%s",
"%s.emails.%s",
"%s-emails.%s",
"emails%s.%s",
"emails.%s.%s",
"emails-%s.%s",
"%ses.%s",
"%s.es.%s",
"%s-es.%s",
"es%s.%s",
"es.%s.%s",
"es-%s.%s",
"%sexport.%s",
"%s.export.%s",
"%s-export.%s",
"export%s.%s",
"export.%s.%s",
"export-%s.%s",
"%sfileshare.%s",
"%s.fileshare.%s",
"%s-fileshare.%s",
"fileshare%s.%s",
"fileshare.%s.%s",
"fileshare-%s.%s",
"%sgcp.%s",
"%s.gcp.%s",
"%s-gcp.%s",
"gcp%s.%s",
"gcp.%s.%s",
"gcp-%s.%s",
"%sgithub.%s",
"%s.github.%s",
"%s-github.%s",
"github%s.%s",
"github.%s.%s",
"github-%s.%s",
"%sgitlab.%s",
"%s.gitlab.%s",
"%s-gitlab.%s",
"gitlab%s.%s",
"gitlab.%s.%s",
"gitlab-%s.%s",
"%sgraphite.%s",
"%s.graphite.%s",
"%s-graphite.%s",
"graphite%s.%s",
"graphite.%s.%s",
"graphite-%s.%s",
"%sgraphql.%s",
"%s.graphql.%s",
"%s-graphql.%s",
"graphql%s.%s",
"graphql.%s.%s",
"graphql-%s.%s",
"%shub.%s",
"%s.hub.%s",
"%s-hub.%s",
"hub%s.%s",
"hub.%s.%s",
"hub-%s.%s",
"%siam.%s",
"%s.iam.%s",
"%s-iam.%s",
"iam%s.%s",
"iam.%s.%s",
"iam-%s.%s",
"%sinfra.%s",
"%s.infra.%s",
"%s-infra.%s",
"infra%s.%s",
"infra.%s.%s",
"infra-%s.%s",
"%sinternal.%s",
"%s.internal.%s",
"%s-internal.%s",
"internal%s.%s",
"internal.%s.%s",
"internal-%s.%s",
"%sinternal-tools.%s",
"%s.internal-tools.%s",
"%s-internal-tools.%s",
"internal-tools%s.%s",
"internal-tools.%s.%s",
"internal-tools-%s.%s",
"%sios.%s",
"%s.ios.%s",
"%s-ios.%s",
"ios%s.%s",
"ios.%s.%s",
"ios-%s.%s",
"%sjira.%s",
"%s.jira.%s",
"%s-jira.%s",
"jira%s.%s",
"jira.%s.%s",
"jira-%s.%s",
"%sjs.%s",
"%s.js.%s",
"%s-js.%s",
"js%s.%s",
"js.%s.%s",
"js-%s.%s",
"%skubernetes.%s",
"%s.kubernetes.%s",
"%s-kubernetes.%s",
"kubernetes%s.%s",
"kubernetes.%s.%s",
"kubernetes-%s.%s",
"%slanding.%s",
"%s.landing.%s",
"%s-landing.%s",
"landing%s.%s",
"landing.%s.%s",
"landing-%s.%s",
"%sldap.%s",
"%s.ldap.%s",
"%s-ldap.%s",
"ldap%s.%s",
"ldap.%s.%s",
"ldap-%s.%s",
"%sloadbalancer.%s",
"%s.loadbalancer.%s",
"%s-loadbalancer.%s",
"loadbalancer%s.%s",
"loadbalancer.%s.%s",
"loadbalancer-%s.%s",
"%slogstash.%s",
"%s.logstash.%s",
"%s-logstash.%s",
"logstash%s.%s",
"logstash.%s.%s",
"logstash-%s.%s",
"%smail.%s",
"%s.mail.%s",
"%s-mail.%s",
"mail%s.%s",
"mail.%s.%s",
"mail-%s.%s",
"%smain.%s",
"%s.main.%s",
"%s-main.%s",
"main%s.%s",
"main.%s.%s",
"main-%s.%s",
"%smanuals.%s",
"%s.manuals.%s",
"%s-manuals.%s",
"manuals%s.%s",
"manuals.%s.%s",
"manuals-%s.%s",
"%smattermost.%s",
"%s.mattermost.%s",
"%s-mattermost.%s",
"mattermost%s.%s",
"mattermost.%s.%s",
"mattermost-%s.%s",
"%smercurial.%s",
"%s.mercurial.%s",
"%s-mercurial.%s",
"mercurial%s.%s",
"mercurial.%s.%s",
"mercurial-%s.%s",
"%smobile.%s",
"%s.mobile.%s",
"%s-mobile.%s",
"mobile%s.%s",
"mobile.%s.%s",
"mobile-%s.%s",
"%smysql.%s",
"%s.mysql.%s",
"%s-mysql.%s",
"mysql%s.%s",
"mysql.%s.%s",
"mysql-%s.%s",
"%sops.%s",
"%s.ops.%s",
"%s-ops.%s",
"ops%s.%s",
"ops.%s.%s",
"ops-%s.%s",
"%soracle.%s",
"%s.oracle.%s",
"%s-oracle.%s",
"oracle%s.%s",
"oracle.%s.%s",
"oracle-%s.%s",
"%spackages.%s",
"%s.packages.%s",
"%s-packages.%s",
"packages%s.%s",
"packages.%s.%s",
"packages-%s.%s",
"%spostgres.%s",
"%s.postgres.%s",
"%s-postgres.%s",
"postgres%s.%s",
"postgres.%s.%s",
"postgres-%s.%s",
"%spresentations.%s",
"%s.presentations.%s",
"%s-presentations.%s",
"presentations%s.%s",
"presentations.%s.%s",
"presentations-%s.%s",
"%spreview.%s",
"%s.preview.%s",
"%s-preview.%s",
"preview%s.%s",
"preview.%s.%s",
"preview-%s.%s",
"%sprivate.%s",
"%s.private.%s",
"%s-private.%s",
"private%s.%s",
"private.%s.%s",
"private-%s.%s",
"%spro.%s",
"%s.pro.%s",
"%s-pro.%s",
"pro%s.%s",
"pro.%s.%s",
"pro-%s.%s",
"%sproducts.%s",
"%s.products.%s",
"%s-products.%s",
"products%s.%s",
"products.%s.%s",
"products-%s.%s",
"%sproject.%s",
"%s.project.%s",
"%s-project.%s",
"project%s.%s",
"project.%s.%s",
"project-%s.%s",
"%spsql.%s",
"%s.psql.%s",
"%s-psql.%s",
"psql%s.%s",
"psql.%s.%s",
"psql-%s.%s",
"%srds.%s",
"%s.rds.%s",
"%s-rds.%s",
"rds%s.%s",
"rds.%s.%s",
"rds-%s.%s",
"%srepo.%s",
"%s.repo.%s",
"%s-repo.%s",
"repo%s.%s",
"repo.%s.%s",
"repo-%s.%s",
"%sscripts.%s",
"%s.scripts.%s",
"%s-scripts.%s",
"scripts%s.%s",
"scripts.%s.%s",
"scripts-%s.%s",
"%ssec.%s",
"%s.sec.%s",
"%s-sec.%s",
"sec%s.%s",
"sec.%s.%s",
"sec-%s.%s",
"%ssecurity.%s",
"%s.security.%s",
"%s-security.%s",
"security%s.%s",
"security.%s.%s",
"security-%s.%s",
"%sservices.%s",
"%s.services.%s",
"%s-services.%s",
"services%s.%s",
"services.%s.%s",
"services-%s.%s",
"%ssitemaps.%s",
"%s.sitemaps.%s",
"%s-sitemaps.%s",
"sitemaps%s.%s",
"sitemaps.%s.%s",
"sitemaps-%s.%s",
"%ssnapshots.%s",
"%s.snapshots.%s",
"%s-snapshots.%s",
"snapshots%s.%s",
"snapshots.%s.%s",
"snapshots-%s.%s",
"%ssource.%s",
"%s.source.%s",
"%s-source.%s",
"source%s.%s",
"source.%s.%s",
"source-%s.%s",
"%ssplunk.%s",
"%s.splunk.%s",
"%s-splunk.%s",
"splunk%s.%s",
"splunk.%s.%s",
"splunk-%s.%s",
"%ssrc.%s",
"%s.src.%s",
"%s-src.%s",
"src%s.%s",
"src.%s.%s",
"src-%s.%s",
"%sstats.%s",
"%s.stats.%s",
"%s-stats.%s",
"stats%s.%s",
"stats.%s.%s",
"stats-%s.%s",
"%ssubversion.%s",
"%s.subversion.%s",
"%s-subversion.%s",
"subversion%s.%s",
"subversion.%s.%s",
"subversion-%s.%s",
"%ssvn.%s",
"%s.svn.%s",
"%s-svn.%s",
"svn%s.%s",
"svn.%s.%s",
"svn-%s.%s",
"%ssyslog.%s",
"%s.syslog.%s",
"%s-syslog.%s",
"syslog%s.%s",
"syslog.%s.%s",
"syslog-%s.%s",
"%steamcity.%s",
"%s.teamcity.%s",
"%s-teamcity.%s",
"teamcity%s.%s",
"teamcity.%s.%s",
"teamcity-%s.%s",
"%stemplates.%s",
"%s.templates.%s",
"%s-templates.%s",
"templates%s.%s",
"templates.%s.%s",
"templates-%s.%s",
"%sterraform.%s",
"%s.terraform.%s",
"%s-terraform.%s",
"terraform%s.%s",
"terraform.%s.%s",
"terraform-%s.%s",
"%straffic.%s",
"%s.traffic.%s",
"%s-traffic.%s",
"traffic%s.%s",
"traffic.%s.%s",
"traffic-%s.%s",
"%straining.%s",
"%s.training.%s",
"%s-training.%s",
"training%s.%s",
"training.%s.%s",
"training-%s.%s",
"%stravis.%s",
"%s.travis.%s",
"%s-travis.%s",
"travis%s.%s",
"travis.%s.%s",
"travis-%s.%s",
"%stroposphere.%s",
"%s.troposphere.%s",
"%s-troposphere.%s",
"troposphere%s.%s",
"troposphere.%s.%s",
"troposphere-%s.%s",
"%suserpictures.%s",
"%s.userpictures.%s",
"%s-userpictures.%s",
"userpictures%s.%s",
"userpictures.%s.%s",
"userpictures-%s.%s",
"%sux.%s",
"%s.ux.%s",
"%s-ux.%s",
"ux%s.%s",
"ux.%s.%s",
"ux-%s.%s",
"%swp.%s",
"%s.wp.%s",
"%s-wp.%s",
"wp%s.%s",
"wp.%s.%s",
"wp-%s.%s",]

for permutation in permutations: 
    print permutation % (target, s3url)


