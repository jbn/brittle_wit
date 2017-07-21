import brittle_wit as bw
from brittle_wit import rest_api as api
from brittle_wit.helpers import grouping as _grouping


async def collect_cursored_ids(ctx, req):
    cursor, ids = bw.Cursor(req), set()

    for page_req in cursor:
        resp = await ctx.execute(page_req)
        ids.update(resp.body['ids'])
        cursor.update(resp)

    return ids


async def collect_follower_ids_for(ctx, screen_name):
    req = bw.rest_api.followers.ids(screen_name=screen_name, count=5000)
    return await collect_cursored_ids(ctx, req)


async def collect_friends_ids_for(ctx, screen_name):
    req = bw.rest_api.friends.ids(screen_name=screen_name, count=5000)
    return await collect_cursored_ids(ctx, req)


async def collect_lists_with_members(ctx, screen_name, only=None):
    req = bw.rest_api.lists.list(screen_name=screen_name)
    lists = (await ctx.execute(req)).body

    for record in lists:
        req = bw.rest_api.lists.members(list_id=record['id'],
                                        slug=record['slug'],
                                        owner_screen_name=screen_name,
                                        count=5000)
        res = await ctx.execute(req)
        record['members'] = [u['screen_name'] for u in res.body['users']]
        record['members_ids'] = [u['id_str'] for u in res.body['users']]

    if only:
        lists = [record for record in lists if record['slug'].lower() in only]

    return lists


async def collect_user_infos_by_ids(ctx, user_ids):
    infos = []

    for i, chunk in enumerate(_grouping(user_ids, 100)):
        print("Collecting chunk {}".format(i))
        req = bw.rest_api.users.lookup(user_id=",".join(str(i) for i in chunk))
        resp = await ctx.execute(req)
        infos.extend(resp.body)

    return infos
