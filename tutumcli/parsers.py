def add_login_parser(subparsers):
    # tutum login
    subparsers.add_parser('login', help='Login into Tutum', description='Login into Tutum')


def add_build_parser(subparsers):
    # tutum build
    build_parser = subparsers.add_parser('build', help='Build an image using an existing Dockerfile, '
                                                       'or create one using buildstep',
                                         description='Build an image using an existing Dockerfile, '
                                                     'or create one using buildstep')
    build_parser.add_argument('-q', '--quiet', help='print minimum information', action='store_true')
    build_parser.add_argument('--no-cache', help='do not use the cache when building the image', action='store_true')
    build_parser.add_argument('-t', '--tag', help='repository name (and optionally a tag) to be applied '
                                                  'to the resulting image in case of success')
    build_parser.add_argument('directory', help='working directory')


def add_service_parser(subparsers):
    # tutum service
    service_parser = subparsers.add_parser('service', help='Service-related operations',
                                           description='Service-related operations')
    service_subparser = service_parser.add_subparsers(title='tutum service commands', dest='subcmd')

    # tutum service run
    create_parser = service_subparser.add_parser('create', help='Create a new service',
                                                 description='Create a new service', )
    create_parser.add_argument('image', help='the name of the image used to deploy this service')
    create_parser.add_argument('-n', '--name', help='a human-readable name for the service '
                                                    '(default: image_tag without namespace)')
    create_parser.add_argument('--cpushares', help='Relative weight for CPU Shares', type=int)
    create_parser.add_argument('--memory', help='RAM memory hard limit in MB', type=int)
    create_parser.add_argument('--privileged', help='Give extended privileges to this container', action='store_true')
    create_parser.add_argument('-t', '--target-num-containers',
                               help='the number of containers to run for this service (default: 1)', type=int,
                               default=1)
    create_parser.add_argument('-r', '--run-command',
                               help='the command used to start the service containers '
                                    '(default: as defined in the image)')
    create_parser.add_argument('--entrypoint',
                               help='the command prefix used to start the service containers '
                                    '(default: as defined in the image)')
    create_parser.add_argument('-p', '--publish', help="Publish a container's port to the host. "
                                                       "Format: [hostPort:]containerPort[/protocol], i.e. \"80:80/tcp\"",
                               action='append')
    create_parser.add_argument('--expose', help='Expose a port from the container without publishing it to your host',
                               action='append', type=int)
    create_parser.add_argument('-e', '--env',
                               help='set environment variables i.e. "ENVVAR=foo" '
                                    '(default: as defined in the image, plus any link- or role-generated variables)',
                               action='append')
    create_parser.add_argument('--tag', help="the tag name being added to the service", action='append')
    create_parser.add_argument('--link-service',
                               help="Add link to another service (name:alias) or (uuid:alias)", action='append')
    create_parser.add_argument('--autorestart', help='whether the containers should be restarted if they stop '
                                                     '(default: OFF)', choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    create_parser.add_argument('--autoreplace', help='whether the containers should be replaced with a new one if '
                                                     'they stop (default: OFF)',
                               choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    create_parser.add_argument('--autodestroy', help='whether the containers should be terminated if '
                                                     'they stop (default: OFF)',
                               choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    create_parser.add_argument('--role', help='Tutum API roles to grant the service, '
                                              'i.e. "global" (default: none, possible values: "global")',
                               action='append')
    create_parser.add_argument('--sequential', help='whether the containers should be launched and scaled sequentially',
                               action='store_true')

    # tutum service inspect
    inspect_parser = service_subparser.add_parser('inspect', help="Get all details from an service",
                                                  description="Get all details from an service")
    inspect_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')

    # tutum service logs
    logs_parser = service_subparser.add_parser('logs', help='Get logs from an service',
                                               description='Get logs from an service')
    logs_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')

    # tutum service ps
    ps_parser = service_subparser.add_parser('ps', help='List services', description='List services')
    ps_parser.add_argument('-q', '--quiet', help='print only long UUIDs', action='store_true')
    ps_parser.add_argument('-s', '--status', help='filter services by status',
                           choices=['Running', 'Partly running', 'Stopped', 'Start failed', 'Stopped with errors'])

    # tutum service redeploy
    redeploy_parser = service_subparser.add_parser('redeploy', help='Redeploy a running service with a '
                                                                    'new version/tag',
                                                   description='Redeploy a running service with a new version/tag')
    redeploy_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')
    redeploy_parser.add_argument('-t', '--tag', help='tag of the image to redeploy')

    # tutum service run
    run_parser = service_subparser.add_parser('run', help='Create and run a new service',
                                              description='Create and run a new service', )
    run_parser.add_argument('image', help='the name of the image used to deploy this service')
    run_parser.add_argument('-n', '--name', help='a human-readable name for the service '
                                                 '(default: image_tag without namespace)')
    run_parser.add_argument('--cpushares', help='Relative weight for CPU Shares', type=int)
    run_parser.add_argument('--memory', help='RAM memory hard limit in MB', type=int)
    run_parser.add_argument('--privileged', help='Give extended privileges to this container', action='store_true')
    run_parser.add_argument('-t', '--target-num-containers',
                            help='the number of containers to run for this service (default: 1)', type=int,
                            default=1)
    run_parser.add_argument('-r', '--run-command',
                            help='the command used to start the service containers '
                                 '(default: as defined in the image)')
    run_parser.add_argument('--entrypoint',
                            help='the command prefix used to start the service containers '
                                 '(default: as defined in the image)')
    run_parser.add_argument('-p', '--publish', help="Publish a container's port to the host. "
                                                    "Format: [hostPort:]containerPort[/protocol], i.e. \"80:80/tcp\"",
                            action='append')
    run_parser.add_argument('--expose', help='Expose a port from the container without publishing it to your host',
                            action='append', type=int)
    run_parser.add_argument('-e', '--env',
                            help='set environment variables i.e. "ENVVAR=foo" '
                                 '(default: as defined in the image, plus any link- or role-generated variables)',
                            action='append')
    run_parser.add_argument('--tag', help="the tag name being added to the service", action='append')
    run_parser.add_argument('--link-service',
                            help="Add link to another service (name:alias) or (uuid:alias)", action='append')
    run_parser.add_argument('--autorestart', help='whether the containers should be restarted if they stop '
                                                  '(default: OFF)', choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    run_parser.add_argument('--autoreplace', help='whether the containers should be replaced with a new one if '
                                                  'they stop (default: OFF)', choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    run_parser.add_argument('--autodestroy', help='whether the containers should be terminated if '
                                                  'they stop (default: OFF)', choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    run_parser.add_argument('--role', help='Tutum API roles to grant the service, '
                                           'i.e. "global" (default: none, possible values: "global")', action='append')
    run_parser.add_argument('--sequential', help='whether the containers should be launched and scaled sequentially',
                            action='store_true')

    # tutum service scale
    scale_parser = service_subparser.add_parser('scale', help='Scale a running service',
                                                description='Scale a running service', )
    scale_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')
    scale_parser.add_argument("target_num_containers", metavar="target-num-containers",
                              help="target number of containers to scale this service to", type=int)
    # tutum service set
    set_parser = service_subparser.add_parser('set',
                                              help='Enable or disable Crash Recovery and Autodestroy features to '
                                                   'an existing service',
                                              description='Enable or disable Crash Recovery and Autodestroy features to'
                                                          ' an existing service')
    set_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')
    set_parser.add_argument('--autorestart', help="whether the containers should be restarted if they stop "
                                                  "(default: OFF)", choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    set_parser.add_argument('--autoreplace', help="whether the containers should be replaced with a new one if "
                                                  "they stop (default: OFF)", choices=['OFF', 'ON_FAILURE', 'ALWAYS'])
    set_parser.add_argument('--autodestroy',
                            help="whether the containers should be terminated if they stop (default: OFF)",
                            choices=['OFF', 'ON_FAILURE', 'ALWAYS'])

    # tutum service start
    start_parser = service_subparser.add_parser('start', help='Start a stopped service',
                                                description='Start a stopped service')
    start_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')

    # tutum service stop
    stop_parser = service_subparser.add_parser('stop', help='Stop a running service',
                                               description='Stop a running service')
    stop_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')

    # tutum service terminate
    terminate_parser = service_subparser.add_parser('terminate', help='Terminate an service',
                                                    description='Terminate an service')
    terminate_parser.add_argument('identifier', help="service's UUID (either long or short) or name", nargs='+')


def add_container_parser(subparsers):
    # tutum container
    container_parser = subparsers.add_parser('container', help='Container-related operations',
                                             description='Container-related operations')
    container_subparser = container_parser.add_subparsers(title='tutum container commands', dest='subcmd')

    # tutum container inspect
    inspect_parser = container_subparser.add_parser('inspect', help='Inspect a container',
                                                    description='Inspect a container')
    inspect_parser.add_argument('identifier', help="container's UUID (either long or short) or name", nargs='+')

    # tutum container logs
    logs_parser = container_subparser.add_parser('logs', help='Get logs from a container',
                                                 description='Get logs from a container')
    logs_parser.add_argument('identifier', help="container's UUID (either long or short) or name", nargs='+')

    # tutum container ps
    ps_parser = container_subparser.add_parser('ps', help='List containers', description='List containers')
    ps_parser.add_argument('-i', '--identifier', help="container's UUID (either long or short) or name")
    ps_parser.add_argument('-q', '--quiet', help='print only long UUIDs', action='store_true')
    ps_parser.add_argument('-s', '--status', help='filter containers by status',
                           choices=['Running', 'Stopped', 'Start failed', 'Stopped with errors'])

    # tutum container start
    start_parser = container_subparser.add_parser('start', help='Start a container', description='Start a container')
    start_parser.add_argument('identifier', help="container's UUID (either long or short) or name", nargs='+')

    # tutum container stop
    stop_parser = container_subparser.add_parser('stop', help='Stop a container', description='Stop a container')
    stop_parser.add_argument('identifier', help="container's UUID (either long or short) or name", nargs='+')

    # tutum container terminate
    terminate_parser = container_subparser.add_parser('terminate', help='Terminate a container',
                                                      description='Terminate a container')
    terminate_parser.add_argument('identifier', help="container's UUID (either long or short) or name", nargs='+')


def add_image_parser(subparsers):
    # tutum image
    image_parser = subparsers.add_parser('image', help='Image-related operations',
                                         description='Image-related operations')
    image_subparser = image_parser.add_subparsers(title='tutum image commands', dest='subcmd')

    # tutum image list
    list_parser = image_subparser.add_parser('list', help='List private images',
                                             description='List private images')
    list_parser.add_argument('-q', '--quiet', help='print only image names', action='store_true')

    list_exclusive_group = list_parser.add_mutually_exclusive_group()
    list_exclusive_group.add_argument('-j', '--jumpstarts', help='list jumpstart images', action='store_true')
    list_exclusive_group.add_argument('-l', '--linux', help='list linux images', action='store_true')

    # tutum image register
    register_parser = image_subparser.add_parser('register',
                                                 help='Register an image from a private repository in Tutum',
                                                 description='Register an image from a private repository in Tutum')
    register_parser.add_argument('image_name', help='full image name, i.e. quay.io/tutum/test-repo')
    register_parser.add_argument('-d', '--description', help='Image description')

    # tutum image push
    push_parser = image_subparser.add_parser('push', help='Push a local image to Tutum private registry',
                                             description='Push a local image to Tutum private registry')
    push_parser.add_argument('name', help='name of the image to push')
    push_parser.add_argument('--public', help='push image to public registry', action='store_true')

    # tutum image rm
    rm_parser = image_subparser.add_parser('rm', help='Deregister a private image from Tutum',
                                           description='Deregister a private image from Tutum')
    rm_parser.add_argument('image_name', help='full image name, i.e. quay.io/tutum/test-repo', nargs='+')

    # tutum image search
    search_parser = image_subparser.add_parser('search', help='Search for images in the Docker Index',
                                               description='Search for images in the Docker Index')
    search_parser.add_argument('query', help='query to search')

    # tutum image update
    update_parser = image_subparser.add_parser('update', help='Update a private image',
                                               description='Update a private image')
    update_parser.add_argument("image_name", help="full image name, i.e. quay.io/tutum/test-repo", nargs="+")
    update_parser.add_argument('-u', '--username', help='new username to authenticate with the registry')
    update_parser.add_argument('-p', '--password', help='new password to authenticate with the registry')
    update_parser.add_argument('-d', '--description', help='new image description')


def add_node_parser(subparsers):
    # tutum node
    node_parser = subparsers.add_parser('node', help='Node-related operations', description='Node-related operations')
    node_subparser = node_parser.add_subparsers(title='tutum node commands', dest='subcmd')

    # tutum node inspect
    inspect_parser = node_subparser.add_parser('inspect', help='Inspect a node', description='Inspect a node')
    inspect_parser.add_argument('identifier', help="node's UUID (either long or short)", nargs='+')

    # tutum node list
    list_parser = node_subparser.add_parser('list', help='List nodes', description='List nodes')
    list_parser.add_argument('-q', '--quiet', help='print only node uuid', action='store_true')

    # tutum node rm
    rm_parser = node_subparser.add_parser('rm', help='Remove a node', description='Remove a container')
    rm_parser.add_argument('identifier', help="node's UUID (either long or short)", nargs='+')

    # tutum node upgrade
    upgrade_parser = node_subparser.add_parser('upgrade', help='Upgrade docker daemon on the node',
                                          description='Upgrade docker daemon to the latest version on the node')
    upgrade_parser.add_argument('identifier', help="node's UUID (either long or short)", nargs='+')


def add_nodecluster_parser(subparsers):
    # tutum nodecluster
    nodecluster_parser = subparsers.add_parser('nodecluster', help='NodeCluster-related operations',
                                               description='NodeCluster-related operations')
    nodecluster_subparser = nodecluster_parser.add_subparsers(title='tutum node commands', dest='subcmd')

    # tutum nodecluster create
    create_parser = nodecluster_subparser.add_parser('create', help='Create a nodecluster',
                                                     description='Create a nodecluster')
    create_parser.add_argument('-t', '--target-num-nodes',
                               help='the target number of nodes to run for this cluster (default: 1)', type=int,
                               default=1)
    create_parser.add_argument('name', help='name of the node cluster to create')
    create_parser.add_argument('provider', help='name of the provider')
    create_parser.add_argument('region', help='name of the region')
    create_parser.add_argument('nodetype', help='name of the node type')

    # tutum nodecluster inspect
    inspect_parser = nodecluster_subparser.add_parser('inspect', help='Inspect a nodecluster',
                                                      description='Inspect a nodecluster')
    inspect_parser.add_argument('identifier', help="node's UUID (either long or short)", nargs='+')

    # tutum nodecluster list
    list_parser = nodecluster_subparser.add_parser('list', help='List node clusters', description='List node clusters')
    list_parser.add_argument('-q', '--quiet', help='print only node uuid', action='store_true')

    # tutum nodecluster rm
    rm_parser = nodecluster_subparser.add_parser('rm', help='Remove node clusters', description='Remove node clusters')
    rm_parser.add_argument('identifier', help="node's UUID (either long or short)", nargs='+')

    # tutum nodecluster scale
    scale_parser = nodecluster_subparser.add_parser('scale', help='Scale a running node cluster',
                                                    description='Scale a running node cluster', )
    scale_parser.add_argument('identifier', help="node cluster's UUID (either long or short) or name", nargs='+')
    scale_parser.add_argument("target_num_nodes", metavar="target-num-nodes",
                              help="target number of nodes to scale this node cluster to", type=int)

    # tutum nodecluster provider
    provider_parser = nodecluster_subparser.add_parser('provider', help='Show all available infrastructure providers',
                                                       description='Show all available infrastructure providers')
    provider_parser.add_argument('-q', '--quiet', help='print only provider name', action='store_true')

    # tutum nodecluster region
    region_parser = nodecluster_subparser.add_parser('region', help='Show all available regions')
    region_parser.add_argument('-p', '--provider', help="filtered by provider name (e.g. digitalocean)")

    # tutum nodecluster nodetype
    nodetype_parser = nodecluster_subparser.add_parser('nodetype', help='Show all available types')
    nodetype_parser.add_argument('-p', '--provider', help="filtered by provider name (e.g. digitalocean)")
    nodetype_parser.add_argument('-r', '--region', help="filtered by region name (e.g. ams1)")


def add_tag_parser(subparsers):
    # tutum tag
    tag_parser = subparsers.add_parser('tag', help='Tag-related operations', description='Tag-related operations')
    tag_subparser = tag_parser.add_subparsers(title='tutum tag commands', dest='subcmd')

    # tutum tag add
    add_parser = tag_subparser.add_parser('add', help='Add tags to services, nodes or nodeclusters',
                                          description='Add tags to services, nodes or nodeclusters')
    add_parser.add_argument('-t', '--tag', help="name of the tag", action='append', required=True)
    add_parser.add_argument('identifier', help="UUID or name of services, nodes or nodeclusters", nargs='+')

    # tutum tag list
    list_parser = tag_subparser.add_parser('list', help='List all tags associated with services, nodes or nodeclusters',
                                           description='List all tags associated with services, nodes or nodeclusters')
    list_parser.add_argument('identifier', help="UUID or name of services, nodes or nodeclusters", nargs='+')
    list_parser.add_argument('-q', '--quiet', help='print only tag names', action='store_true')

    # tutum tag rm
    rm_parser = tag_subparser.add_parser('rm', help='Remove tags from services, nodes or nodeclusters',
                                         description='Remove tags from services, nodes or nodeclusters')
    rm_parser.add_argument('-t', '--tag', help="name of the tag", action='append', required=True)
    rm_parser.add_argument('identifier', help="UUID or name of services, nodes or nodeclusters", nargs='+')

    # tutum tag set
    set_parser = tag_subparser.add_parser('set', help='Set tags from services, nodes or nodeclusters',
                                          description='Set tags from services, nodes or nodeclusters. '
                                                      'This will remove all the existing tags')
    set_parser.add_argument('-t', '--tag', help="name of the tag", action='append', required=True)
    set_parser.add_argument('identifier', help="UUID or name of services, nodes or nodeclusters", nargs='+')


def add_webhookhandler_parser(subparsers):
    # tutum webhook-handler
    webhookhandler_parser = subparsers.add_parser('webhook-handler', help='Webhook-handler-related operations',
                                                  description='Webhook-handler-related operations')
    webhookhandler_subparser = webhookhandler_parser.add_subparsers(title='tutum webhook-handler commands', dest='subcmd')

    # tutum webhook-handler create
    create_parser = webhookhandler_subparser.add_parser('create', help='create webhook handler to services',
                                          description='create webhook handler to services')
    create_parser.add_argument('-n', '--name', help="name of the webhook handler (optional)", action='append')
    create_parser.add_argument('identifier', help="UUID or name of services", nargs='+')

    # tutum twebhook-handler list
    list_parser = webhookhandler_subparser.add_parser('list', help='List all webhook handler associated with services',
                                           description='List all webhook handler associated with services')
    list_parser.add_argument('identifier', help="UUID or name of services", nargs='+')
    list_parser.add_argument('-q', '--quiet', help='print only webhook andler uuid', action='store_true')
    
    # tutum webhook-handler delete
    rm_parser = webhookhandler_subparser.add_parser('rm', help='Remove webhook handler to a service',
                                          description='create webhook handler to a service')
    rm_parser.add_argument('identifier', help="UUID or name of services")
    rm_parser.add_argument('webhookhandler', help="UUID or name of the webhook handler", nargs='+')
